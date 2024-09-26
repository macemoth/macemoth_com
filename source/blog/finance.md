---
author: macemoth
language: en
date: 20.04.2022
readtime: 10 min
---

# Ideas from quantitative finance

This site is a notebook for people interested in \{mathematical | computational | quantitative\} finance. Note that it has neither the goal to be accurate nor complete. 

Mathematical finance can be split into:

* Pricing models (i.e. Black-Scholes)
* Risk management (i.e. portfolio optimisation)
* Trading strategies

## Getting Started

If you have an endless supply of time, read John C. Hull, *Options, Futures, and Other Derivatives, Global Edition*. Otherwise, the below "glossary" should get you acquainted with some of the basic concepts of the quant trade. The list is a non-exhaustive work in progress and is biased in the author's interest.

Financial markets are supposed to be [chaotic](https://www.youtube.com/watch?v=fDek6cYijxI). In the seventies, academia was quite confident that financial markets process new information immediately (such as news about a company that may drive a stock higher). It concluded that it would therefore be impossible to predict the market with publicly available information, because the news' consequences are immediately absorbed by the market. They called such markets [efficient markets](https://en.wikipedia.org/wiki/Efficient-market_hypothesis). In this view, the market can be represented by a [random walk](https://en.wikipedia.org/wiki/Random_walk). To consistently make profit in an efficient market requires exploiting inefficiencies or insider information.

However,  MIT's [Topics in Mathematics with Applications in Finance](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/) course suggests that efficient markets are a theoretical construct, and in reality there are inefficiencies exploitable by sophisticated algorithms.

A more primitive way to model derivatives are binomial trees, that represent the two outcomes of options (look at [Sal Khan's excellent series about options](https://www.youtube.com/playlist?list=PL55F11C99198EAE65) or read Hull's Book P. 34ff).

## Epilogue

When speaking about random walks, the notion of [Hidden Markov Models](https://en.wikipedia.org/wiki/Hidden_Markov_model) may come to mind. Their parameters are found using [Baum-Welch's Algorithm](https://en.wikipedia.org/wiki/Baum%E2%80%93Welch_algorithm), similar to Gaussian Mixture Models. [Bayesian Networks](https://en.wikipedia.org/wiki/Bayesian_network) also sound interesting, as they seem to approximate probabilities instead of computing them exactly.

Recently, quantum computers have been studied to do exactly this Monte Carlo part faster than classical computers (which is highly interesting, and referred below). Also, I wonder whether the Monte Carlo Tree Search (highly effective in Chess programs) or other Learning Algorithms could be used to evaluate binomial trees.


## Further Reading and ideas

- Nicholas Nassim Taleb's, *The Black Swan*, is a sceptical view on the "standard" mathematical approaches and epistemological problems when modelling reality.
- [Patrick Rebentrost et al., *Quantum computational finance: Monte Carlo pricing of financial derivatives*](https://arxiv.org/pdf/1805.00109) demonstrates how to do the Monte-Carlo part (faster) with a quantum computer. Something I have yet to dive into.
- [finmath](http://www.finmath.net) seems to be an interesting Java implementation of various financial algorithms and data structures. They have interesting examples on their website.
- [JQuantLib](http://www.jquantlib.com/en/latest/) is another one.
- The MIT [Topics in Mathematics with Applications in Finance](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/) course is a nice companion to this
- [Wired article](https://www.wired.com/2016/01/the-rise-of-the-artificially-intelligent-hedge-fund/) about algorithmic trading and the use of new methods
- As the financial market is a highly interconnected system, Gaussian models often do not hold (as they arise with independence) ideas from biology and ecology may apply. One paradigm to examine may be [Chaos Theory](https://en.wikipedia.org/wiki/Chaos_theory).

## YOLO 🚀🌕 Meme Corner

- [Barclays Robin Hood Explotation Strategy](https://www.youtube.com/watch?v=8pYgz4YlQnE) 



