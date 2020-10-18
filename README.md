# SciPy Japan 2020 - (D)Ask Me Anything About Data Analysis at Scale?

Welcome to (D)Ask Me Anything About Data Analytics at Scale, where we will be going over some techniques for preparing large datasets for analysis and, of course, analysing them as well (who wants to just clean data for about 4 hours anyways). I mean, is not like data analytics/science projects often go by the 80-20 rule, 80% cleaning, prepering and engineering features, and 20% modeling, testing hypotheses and making predictions.

Just for the fun of it, you can also refer to this tutorial by what is not commonly known as HPC, which is short for **High Performance Cleaning**.

The work in this tutorial is inspired on a project I have been working on during my tenure at INSEAD. The data involves over 1 terabyte of job descriptions from job ads in the US over the last 13 years. The complexity, messiness, and stubborness of these data, would have been untamable and downright painful without Dask and a few other libraries in the data science ecosystem/repertoire.

Unfortunately, and at the same time to your benefit, I was not allowed to use the data from my project for this tutorial so instead, we will travel together across the world and build our own Airbnb data science project by the end of the tutorial.

# Table of Contents

1. Tutorial Structure and The **Why** behind this tutorial
2. Learning Outcomes
3. What this tutorial is not about
4. Prerequisites
5. Getting Started
6. Data
7. Notebooks
    - 00 Getting the Data
    - 01 Cleaning & Reshaping it
    - 02 Analyzing it
    - 03 Predicting from it
    - 04 Tips and Trics
8. Test your understanding
9. Acknowledgements
10. Additional Resources
11. Feedback (arigatōgozaimashita) 😃


## 1a. Tutorial Structure

We will follow the following schedule throughout the tutorial, as best as possible.
- 9:00 - 9:35 (JST) intro/setup
- 9:35 - 9:40 (JST) short break
- 9:40 - 10:45 (JST) instructions
- 10:45 - 11:00 (JST) long break
- 11:00 - 11:45 (JST) instructions
- 11:45 - 11:50 (JST) short break
- 11:50 - 12:30 (JST) instructions

### 1b. The Why behind this tutorial

Have ever heard from experienced data professionals that only a small amount of data is needed in order to get started and get a few files worth of good/usuable code that can be extended later on to the full dataset? (a mouthful question, I know, stay with me). If so, they are probably right! But, what happens when your data is massive, tabular, and with a lot of textual columns that may have one, two, or a thousand edge cases that you may not be able to identify/anticipate without having a look at the entire dataset? For those instances, the python data science community has come up with fantastic tools to help us do data analysis at scale.

In this tutorial, we will get to explore how to tackle this issue of having a lot of data that does not fit into memory and needs to be cleaned and shaped into form before we can extract meaningful insights from it.


## 2. Learning Outcomes

It is okay to not understand absolutely everything in the tutorial, instead, I would like to challenge you to first, make sure you walk away with at least 2 new (for you) concepts from this lesson, and second, that you come back to it and go over the content you did not get the first time around.

With that said, by the end of the tutorial you should be able to:

1. Understand the data analytics cycle.
2. Diffferentiate between small, medium and large datasets.
3. Understand how to gather, clean, and process data.
4. Analyse and visualise different data sets.
5. Have a project to showcase.
6. Keep doing good things with data at scale. 😃


## 3. What this tutorial is not about

1. Although it is tailored towards beginners in this topic, this is not an introduction to Python. If you have never written a line of code, this is not the right tutorial for you, that's the one we had yesterday. :)
2. This is not an Artificial Intelligence tutorial, that one is running right now as well. :)
3. This is not a web scraping tutorial, although we will do some of that.
4. This is not a tutorial covering every feature of Dask. We will mainly use the Dataframe API to clean, process, and analyse our data.

## 4. Prerequisites (P) and Good To Have (GTH)

- **(P)** Attendees for this tutorial are expected to be familiar with Python (1 year of coding would be fantastic). 
- **(P)** Ideally, you are comfortable with loops, functions, lists comprehensions, and if-else statements (i.e. control flow).
- **(GTH)** While it is not necessary to have knowledge of NumPy and pandas, a bit of experience with these two libraries will be very beneficial throughout this tutorial
- **(P)** You should have at least 10 GB of free memory in your computer. We will not use that much, of course, (at best 3 or 4), but it would be best to avoid downloading 4 GB and then having your computer yell at you because it doesn't have enough space available.

## 5. Getting Started

You should first make sure you have [Anaconda](https://www.anaconda.com/products/individual#download-section) or Miniconda installed. This will allow you to have most of the things you will need for this tutorial already installed once you open up Jupyter Lab.

Here are some of the ways in which you can get set up.

### First Step

Open up your terminal and navigate to a directory of your choosing in your computer. Once there, run the following command.

```sh
 git clone https://github.com/ramonprz01/scipy_20jp_dask.git
```

Conversely, you can click on the green `downlowad` button at the top and donwload all files to your desired folder/directory.

### Second Step

To get all dependancies, packages and everything else that would be useful in this tutorial, you can recreate the environment with the following lines:

```sh
cd scipy_20jp_dask
conda env create -f environment.yml
```

### Third Step

Then you will need to activate your environment using the following command, and then open up jupyter lab.

```sh
conda activate dask_tutorial_env
jupyter lab
```

Great work! Now navigate to notebook 00 and open it.

## 6. Data

We will be using Airbnb data collected by a scraping tool called Inside Airbnb