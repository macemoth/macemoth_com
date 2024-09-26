from jinja2 import Environment, FileSystemLoader, select_autoescape
import sys
import os
import markdown
import shutil
import frontmatter
from datetime import datetime

# Define menu and general settings
menu = []
site = {"baseurl":"macemoth", "title":"macemoth.com", "menu":menu}

def main(source, target):
    # Load templates
    env = Environment(loader=FileSystemLoader("templates"))
    art_template = env.get_template("article.html")
    fourofour_template = env.get_template("404.html")
    front_template = env.get_template("front.html")
    blog_template = env.get_template("blog.html")

    # Define fixed pages
    front_page = {"title": "Home", "content": ""}
    blog_page = {"title": "Blog", "content": ""}
    fourofour_page = {"title": "404", "content": "This page does not exist"}
    sitemap = {"title": "Sitemap", "content": ""}

    # Create target dirs and copy data
    initialise_structure(target)
  
    # Process blog sites
    documents = []
    for f in os.listdir(os.path.join(source, "blog")):
        page = get_page(os.path.join(source, "blog", f))
        if page == {}:
            continue
        if page["fname"] in ["faq", "disclaimer"]:
            pass
        else:
            documents.append(page)
        documents.sort(key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"), reverse=True)
        doc_html = art_template.render(page=page, site=site)
        write_file(os.path.join(target, "blog", f"{page['fname']}.html"), doc_html)
        
    # Process front page
    front_page = get_page(os.path.join(source, "index.md"))
    write_file(os.path.join(target, "index.html"), front_template.render(page=front_page, site=site))

    # Process blog page
    blog_page = get_page(os.path.join(source, "index.md"))
    blog_page["posts"] = documents
    write_file(os.path.join(target, "blog", "index.html"), blog_template.render(page=blog_page, site=site))
    
    # Write 404 page
    write_file(os.path.join(target, "404.html"), fourofour_template.render(page=fourofour_page, site=site))
    
    # Process sitemap
    sitemap["content"] = make_sitemap(documents)
    write_file(os.path.join(target, "sitemap.html"), art_template.render(page=sitemap, site=site))


def initialise_structure(target):
    for d in ["css", "img", "files", "fonts"]:
        shutil.copytree(d, os.path.join(target, d), dirs_exist_ok=True)
    os.makedirs(os.path.join(target, "blog"), exist_ok=True)

        
        
def get_page(f):
    name = f.split("/")[-1][:-3]
    suffix = f[-3:]
    if suffix != ".md":
        return {}
    metadata, md = frontmatter.parse(read_file(f))
    title = md.split("\n")[0].replace("# ", "")
    if len(title) < 3:
        title = name
    html = markdown.markdown(md, extensions=["footnotes", "fenced_code"])
    page = {"title": title, "content": html, "md": md, "fname": name}
    page.update(metadata) # load remaining attributes into page
    return page
    
def get_featured_pages(documents, k):
    featured = []
    for i in range(k): # with replacement
        a = documents[random.randint(0, len(documents)-1)]
        words = a["md"].split(" ")
        a["excerpt"] = " ".join(words[1:min(len(words), 20)]) + "..."
        featured.append(a)
    return featured

    
def make_sitemap(documents):
    md = ["# Sitemap"]
    md.append("**[Home](.)**")
    for page in menu:
        md.append(f"**[{page['title']}]({page['fname']}.html)**")
    
    md.append(f"**Posts**")
    
    for doc in sorted(documents, key=lambda d: d['title']):
        md.append(f"- [{doc['title']}]({doc['fname']}.html)")
    sitemap = "\n\n".join(md)
    return markdown.markdown(sitemap)

def read_file(path):
    with open(path, "r") as file:
        raw = file.read()
        file.close()
        return raw
        
def write_file(path, content):
    with open(path, "w") as file:
        file.write(content)
        file.close()

if __name__ == "__main__":
    source, target = sys.argv[1], sys.argv[2]
    main(source, target)



