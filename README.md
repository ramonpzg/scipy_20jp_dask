# SciPy Japan 2020 - (D)Ask Me Anything About Data Analysis at Scale?

Welcome to (D)Ask Me Anything About Data Analytics at Scale, where we will be going over some techniques for preparing large datasets for analysis and, of course, analysing them as well (who wants to just clean data for about 4 hours anyways).

Just for the fun of it, you can also refer to this tutorial by what is not commonly known as HPC, which is short for **High Performance Cleaning**.

The work in this tutorial is inspired on a project I have been working on during my tenure at INSEAD. The data involves over 1 terabyte of job descriptions from job ads in the US over the last 13 years. The complexity, messiness, and stubborness of these data, would have been untamable without Dask and a few other libraries in the data science repertoire.

Unfortunately and at the same time to the benefit of the audience, I wasn't allowed to use the data for this tutorial, so instead, we will travel together across the world and build our own Airbnb data science project by the end of the tutorial.

# Table of Contents

1. Tutorial Structure and Questions we will work through
2. Learning Outcomes
3. The Why behind this tutorial
4. What this tutorial is not about
5. Things you will need for this tutorial
6. Data
7. Notebooks
    - 00 Getting the Data
    - 01 Cleaning it
    - 02 Reshaping it
    - 03 Analyzing it
    - 04 Predicting from it
    - 05 Tips and Trics
8. Test your understanding
9. Additional Resources
10. Feedback (arigatōgozaimashita) 😃


## 1. Tutorial Structure and Questions we will work through

## 2. Learning Outcomes

It is 100% okay to not understand absolutely everything in the tutorial, instead, I would like to challenge you to first, make sure you walk away with at least 2 important concepts from this lesson, and second, that you come back to it and go over the content again. The second time around, make sure you get even more out of it that you did the first time.

With that said, by the end of the tutorial you should be able to:

1. Understand the data analytics cycle
2. Diffferentiate between small, medium and large datasets
3. Understand how to gather, clean, and process data
4. Analyse and visualise different data sets
5. Have a project to showcase
6. Keep doing good things with data 😃

## 3. The Why behind this tutorial

Have ever heard from experienced data professionals that only a small amount of data is needed in order to get started and get a few files worth of good and usuable code that can be extended later on to the full dataset? If so, chances are, they are probably right! But, what happens when your data is massive, tabular, and with a lot of textual columns that might have one, two, or a thousand edge cases that you might not be able to identify without having a look at the entire dataset? For those instances, the python and the data science community within it have come up with fatntastic tools to help with this endeavor. In this tutorial, we will get to explore how to tackle this issue and 





## What this tutorial is not

1. Although it is tailored towards beginner in this topic, this is not an introduction to Python. If you have never written a line of code, this is not the right tutorial for you, that's the one you we had yesterday :)
2. This is not an Artificial Intelligence tutorial, that's the next one :)
3. This is not a web scraping tutorial, although we will do some of that
4. 