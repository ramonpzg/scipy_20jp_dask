# (D)Ask Me Anything About Data Analysis at Scale?

## SciPy Japan 2020

Welcome to (D)Ask Me Anything About Data Analytics at Scale, where we will be going over some techniques for preparing large datasets for analysis and, of course, analysing the datasets as well (who wants to just clean data for about 4 hours anyways).

Just for the fun of it, you can also refer to this tutorial by what is not commonly known as HPC, which is short for **High Performance Cleaning**.

The work in this tutorial was inspired on a project I have been working on this year at INSEAD. The data involves over 1 terabyte of job descriptions from ads in the US over the last 13 years. The complexity, messiness, and stubborness of these data would have been untamable and downright painful without Dask and a few other libraries in the data science ecosystem/repertoire.

While I would have loved to use the data I've been working with for this tutorial, we will travel together across the world and build our own Airbnb data analytics project in the next 4 hours together.

# Table of Contents

1. Tutorial Structure and The **Why** behind this tutorial
2. Learning Outcomes
3. What this tutorial is not about
4. Prerequisites
5. Getting Started
6. Data
7. Notebooks
    - 00 Setting the Stage and Getting the Data
    - 01 Deep Cleaning
    - 02 Reshaping
    - 03 Analysis
    - 04 Building a Data Product
8. Acknowledgements
9. Additional Resources
10. Feedback (arigatōgozaimashita) 😃


## 1a. Tutorial Structure

We will (as best as we can) follow the following schedule throughout the tutorial.
- 9:00 - 9:35 (JST) intro/setup
- 9:35 - 9:40 (JST) short break
- 9:40 - 10:45 (JST) instructions
- 10:45 - 11:00 (JST) long break
- 11:00 - 11:45 (JST) instructions
- 11:45 - 11:50 (JST) short break
- 11:50 - 12:30 (JST) instructions

## 1b. The Why behind this tutorial

Have ever heard from experienced data professionals that only a small amount of data is needed in order to get started and create a few files worth of good/usuable code that can be extended later on to the full dataset? (a mouthful question, I know, stay with me). If so, these are probably right! But, what happens when your data is massive, tabular, and with a lot of text-based columns that may have one, two, or a thousand edge cases that you may not be able to identify/anticipate without having a look at the entire dataset? For those instances, we have some great tools that the python data science community has come up with and will help up take care of massive and messy datasets relatively fast.

In this tutorial, we will explore how to tackle this issue of having a lot of data that does not fit into memory and needs to be cleaned and reshaped into form before we can extract meaningful insights from it.


## 2. Learning Outcomes

It is okay to not understand absolutely everything in the tutorial, instead, I would like to challenge you to first, make sure you walk away with at least 2 new concepts from this lesson, and second, that you come back to it and go over the content you did not get the first time around.

With that said, by the end of the tutorial you should be able to:

1. Understand the data analytics cycle.
2. Diffferentiate between small, medium and big datasets.
3. Understand how to gather, clean, and process large amounts of data.
4. Analyse and visualise large datasets.
5. Have a canvas for a data analytics project you could showcase.
6. Keep doing good things with data at scale. 😃


## 3. What this tutorial is not about

1. Although it is tailored towards beginners in this topic, this is not an introduction to Python. If you have never written a line of code, this is not the right tutorial for you, that's the one we had yesterday. :)
2. This is not an Artificial Intelligence tutorial, that one is running right now as well. :)
3. This is not a web scraping tutorial, although we will do some of that today.
4. This is not a tutorial covering every feature of Dask. We will mainly use the Dataframe API to clean, process, and analyse tabular data.

## 4. Prerequisites (P) and Good To Have (GTH)

- **(P)** Attendees for this tutorial are expected to be familiar with Python (1 year of coding would be ideal). 
- **(P)** Ideally, you are comfortable with loops, functions, lists comprehensions, and if-else statements (i.e. control flow).
- **(GTH)** While it is not necessary to have knowledge of NumPy and pandas, a bit of experience with these two libraries will be very beneficial throughout this tutorial.
- **(P)** You should have at least 10 GB of free memory in your computer. We will not use that much, of course, (at most between 3 and 5), but it would be best to avoid downloading 4 GB and then having your computer yell at you because it doesn't have enough space available.
- **(GTH)** Make sure to close out any applications, tabs, and programs you might have running in the background and only leave open what you need for the tutorial open and readily available.

## 5. Getting Started

You should first make sure you have [Anaconda](https://www.anaconda.com/products/individual#download-section) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed. This will allow you to have most of the packages you will need for this tutorial already installed once you open up Jupyter Lab.

Here are some of the ways in which you can get set up.

### 5.1 Option 1

#### First Step

Open up your terminal and navigate to a directory of your choosing in your computer. Once there, run the following command.

```sh
 git clone https://github.com/ramonprz01/scipy_20jp_dask.git
```

Conversely, you can click on the green `downlowad` button at the top and donwload all files to your desired folder/directory.

#### Second Step

To get all dependancies, packages and everything else that would be useful in this tutorial, you can recreate the environment with the following lines:

```sh
cd scipy_20jp_dask
conda env create -f environment.yml
```

#### Third Step

Then you will need to activate your environment using the following command, and then open up jupyter lab.

```sh
conda activate dask_tutorial_env
jupyter lab
```

### 5.2 Option 2

#### First Step

Download the repo using the big green button on the upper right.

![green button](images/repo.png)

#### Second Step

Open a Jupyter Lab session inside the folder you just downloaded. Conversely, open a Jupyter Lab session anywhere you'd like and navigate to the folder you just downloaded.

#### Third Step

Open up a terminal inside of Jupyter Lab and run either of the following commands.

```sh
## one option
pip install -U pandas numpy dask bokeh pyarrow parquet python-graphviz matplotlib altair scipy seaborn

## another option
conda install numpy pandas matplotlib scipy bokeh dask distributed -c conda-forge

```

Great work! Now navigate to notebook 00 and open it.

## 6. Data

![inside_airbnb](../images/inside_airbnb.png)

We will be using Airbnb data collected by a scraping tool called [Inside Airbnb](http://insideairbnb.com/about.html). The tool periodically scrapes data from Airbnb and publishes it for free on its website.

The data differs slightly (or by a lot) from country to country, and from time-frame to time-frame. Niether fact should be surprising, the former my be due to different countries having different regulations that may or may not prevent Airbnb from posting the same information regarding a listing. The latter makes sense as we would expect Airbnb to continue improving its business from year-to-year and change the information collected from a host and displayed on a listing.

If you have any issues with getting the data during the session, for any particular reason, you can come back to this README file and access all of the files using the link below.

> ### [LINK to the Data](https://web.tresorit.com/l/A9BNp#CLauHij6y1kKsDDPMizJlA)


## 7. Notebooks

The tutorial is organized in the following notebooks. Notebooks 00 through 02 form the core of this tutorial, and are guaranteed to be covered throughout today's session. Anything beyond that will be treated as additional (fun) material that I hope you will find useful beyond today's session.

- 00 Setting the Stage and Getting the Data
- 01 Deep Cleaning
- 02 Reshaping
- 03 Analysing
- 04 Building a Data Product


## 8. Acknowledgements

The work in this tutorial was made possible because of the many talented people who have invested valuable time and effort in building these great tools for the Python ecosystem. So many thanks to pandas, NumPy, and Dask teams. Also, many thanks to Garret Blankenship. Without his help, lesson 00 would have taken the entire 4 hours of the tutorial.

## 9. Additional Resources

Here are a few great resources to get started with data analytics, large scale data analysis, and data science regardless if this was your first time learning some of the concepts and techniques in these fields.

- [Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=quantpytho-20&creative=9325&linkCode=as2&creativeASIN=1491957662&linkId=ea8de4253cce96046e8ab0383ac71b33) by Wes McKinney
- [Data Science with Python and Dask](https://www.amazon.com/Data-Science-Scale-Python-Dask/dp/1617295604) by Jesse C. Daniel
- [Data Science from Scratch](https://www.amazon.com/_/dp/1492041130?tag=oreilly20-20) by Joel Grus
- [Python Machine Learning](https://www.packtpub.com/product/python-machine-learning-third-edition/9781789955750) by Sebastian Raschka
- [Fast.ai Courses and Book](https://www.fast.ai/)

## 10. Feedback (arigatōgozaimashita) 😃

If you could please help me make this tutorial a better one with your feedback, I would very much appreciate it.

> # [Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLScBo_oOdrpmYztm-PzeSgXU6sbxSp-9dOJxXVg1Rd8EnSY9AQ/viewform?usp=sf_link)