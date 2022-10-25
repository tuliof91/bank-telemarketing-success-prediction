# Bank telemarketing success prediction

## Purpose

This is an end-to-end machine learning project and also an introductory guide on how to write production ready code and how to deploy machine learning models.

We will also review basic concepts such as how to check data quality and how to build models, but more emphasis will be placed on these engineering topics:

- Version control with Git and GitHub
- Packages and environment management with Conda
- Object-Oriented Programming
- Artifact and parameter tracking with MLflow
- Developing packages with reusable components
- Unit Tests
- Docker containers
- Flask APIs

# Goal

The goal of this project is to create a process for creating a data science model using code that is *reliable*, *reproducible* and *easy to iterate on*

# The dataset

For the purpose of this project, we will use the [Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing), specifically we will be using the `bank-additional-full.csv` file.

This is a relatively clean dataset with a clear outcome variable. Using a simple dataset is great to use in a case study that focuses more on engineering and building reliable, reproducible code than cleaning data and extracting insights.

This data comes from marketing phone calls that were made by a Portuguese bank. The target variable indicates whether the person that received the phone call put a deposit in the bank or not. Some other variables include the age, job, education level, and marital status of the person who received the phone call.

# Follow along

I encourage you to follow along with me on this en-to-end project. In case you are familiar with the concepts covered, I suggest you write your own code in the same steps I'm taking. 

Trust me, applying these concepts on your own code will greatly improve your learning curve.

This project follows the structure below, and I will be covering a gentle introduction on each of these topics followed by an implementation of these concepts to the project.

## Topics

1. [Creating a GitHub Repository](https://github.com/tuliof91/bank-telemarketing-success-prediction/blob/main/tutorials/01-github-basics.md)
2. Setting up a conda environment
3. Checking data quality
4. Creating a python package
5. Unit tests for data science
6. Object oriented programming in python
7. Tracking data with MLflow
8. Tracking models with MLflow
9. Serving models with Flask