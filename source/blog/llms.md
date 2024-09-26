---
author: macemoth
language: en
date: 10.07.2023
readtime: 2 min
---

# Large Language Models simulate thinking

In a recent talk[^1], Andrej Karpathy, of one of the co-founders of *OpenAI*, the organisation behind GPT and ChatGPT, discussed several key differences between large language models (LLMs) such as GPT or Llama to human thinking.
There is a deeper rationale behind the discussion -- as LLMs are marketed as the spearhead of "Artificial Intelligence", it makes sense comparing them to the best known "Natural Intelligence".
This article is a reflection on the talk, summarising some of the most interesting questions.

More striking than the differences, many of which have been pointed out in the recent months, are the similarities. That despite the simple abstraction[^2] of predicting the next character based on the previous context, the appearance of thinking emerges. That, without ever having been specifically instructed to do so, the models can be tricked into being personal assistants in a dialogue scenario.

## What's the big deal?

Do the models fabricate information? Yes. Are they overparametrised? Probably. Can they compete with humans in general tasks?
Also yes. GPT-4, OpenAI's most recent model, managed to rank among the best 20% of test takers in a wide range of University-level exams. It is knowledgeable about a comprehensive volume of knowledge (i.e. give a list of technologies of *Sid Meier's Alpha Centauri* along with the in-game description), summarise mathematical research papers[^3] and write correct computer code from a natural language description.

## Thought chains

Some of the notable differences between LLM text generation and human thought are the lack of reflection, not knowing what they don't know, or correcting mistakes while thinking (or generating text, respectively).
Yet, similarly to being an assistant, the models can be tricked into producing a chain of thought while writing text by prompting it to process step-by-step.
By forcing the the model produce a chain of thought, some of the previous problems can be fixed. More importantly, the model simulates human thinking by producing what Karpathy calls "internal monologue".

This is reminiscent to physicist Enrico Fermi's question: How many piano tuners are there in Chicago?
Typically, one can not answer the question directly, but one can arrive at a guess by combining known things, such as the population of Chicago, the amount of pianos, the time it takes to tune a piano, etc.

After all, the LLM's only inherent goal is to faithfully reproduce the training data, not necessarily be reflective or critical. But if the models are asked for, they can do so, just as they become assistants after they are asked to (ChatGPT does this in the background).
This coincides with the observation that LLMs produce better answers when provided with much text from an user - the model just needs to be brought into the right state of mind.

## The way ahead

Instructing LLMs to do things that humans do intuitively may not be the mitigation to the problems of current-day LLMs.
Combining a thought with a previous experience that does not appear in the recent context is more difficult to deal with - although not impossible.
Enhancing the working memory of LLMs with data from the Internet, own documents, databases and vector stores are promising approaches.
[LLamaIndex](https://gpt-index.readthedocs.io) and [LangChain](https://langchain.readthedocs.io) provide powerful connectors to data sources and sophisticated abstractions.

Whether LLMs will be able to perform non-obvious "concept-jumps" (a quality associated with scientific discovery and invention) is still an open question, and the answer will likely either require or bring a deeper undestanding of intelligence.
For the moment, let's ride the wave and see how far LLMs will bring us in computational intelligence.


[^1]: Andrej Karpathy, [State of GPT, May 2023](https://karpathy.ai/stateofgpt.pdf)

[^2]: Generating text by predicting the next characters is not new. In the 1980s, Bell Labs scientists [faked a human user in newsgroups](https://en.wikipedia.org/wiki/Mark_V._Shaney) by simply predicting a likely word from a single preceding word. The texts are surprisingly consistent.

[^3]: Terence Tao, [Embracing change and resetting expectations](https://unlocked.microsoft.com/ai-anthology/terence-tao/)




