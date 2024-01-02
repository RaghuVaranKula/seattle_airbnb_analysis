# Airbnb Seattle Analysis
This project focuses on analyzing Airbnb data for Seattle to gain valuable insights into various aspects of the rental market. We aim to answer several key questions and provide data-driven findings to enhance understanding.

# Table of Contents
Introduction
Data
Analysis Questions
Methodology
Results
Conclusion
Contributing
License


# Introduction
Airbnb is a popular platform for both hosts and travelers. This analysis delves into the Seattle Airbnb market with a focus on answering the following questions:

1)How does the availability of properties on Airbnb vary by month in a single year?
2)If availability is treated as occupancy, what would be the revenue for each month in that year?
3)How does the rent price per day vary for different properties?
4)What is the relationship between property types and rent price per day for those willing to spend up to $100?
5)Can a model be developed to predict property prices using data from the 'listings.csv' file, and what factors influence the price?
6)Which are the top 15 listings on Airbnb with the most reviews?
7)What insights can be drawn about overall guest satisfaction and listing performance using mean, median, and standard deviation metrics?

# Data
Our analysis is based on the Airbnb Seattle dataset, which can be found here. This dataset contains information about listings, reviews, and calendar data.

# Analysis Questions
We will address the following questions in our analysis:

# 1) Availability Analysis:
Explore how property availability varies by month in a single year.

# 2)Revenue Calculation:
Calculate potential revenue based on availability data.

# 3)Rent Price Variation:
Analyze how the rent price per day varies among different properties.

# 4)Property and Price Relationship:
Examine the relationship between property types and rent price per day for those with a budget of up to $100.

# 5)Price Prediction Model:
Build a predictive model for property prices using data from 'listings.csv' and identify influential factors.

# 6)Top 15 Listings:
Identify and present the top 15 Airbnb listings with the most reviews.

# 7)Guest Satisfaction Analysis:
Provide insights into overall guest satisfaction and listing performance using mean, median, and standard deviation metrics.


# Methodology
Our analysis will involve data preprocessing, exploratory data analysis, statistical modeling, and visualization. Python and relevant libraries (e.g., Pandas, Matplotlib, Seaborn, Scikit-Learn) will be used for data manipulation, analysis, and visualization.

# Results
The findings and results for each question will be presented in separate sections of the analysis report. Visualizations, statistical summaries, and insights will be provided to address each question.

# Conclusion
This project aims to deliver data-driven insights into the Seattle Airbnb market, addressing various aspects of property availability, pricing, and guest satisfaction. The analysis results will contribute to a better understanding of the rental market in the city.

# Contributing
If you would like to contribute to this project or have suggestions, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.























# seattle_airbnb_analysis
The Seattle Airbnb homes data

# Table of contents
Project_1.py, source code for all images and results.

# Unlocking Insights: A Deep Dive into Data Analysis
1) Which is the best month for sales in 2016-2017 for Airbnb?
2) When will be the 75% lower price properties available?
3) How much property is with instant booking avilabililty	and flexible cancellation policy?
4) Which month has 75% higher value properties available to the awarness of customers?
5) Which month has most availability of properties?
6) Which property has most reviews?

# Installation
Additional library requirements can be found in 'requirements.txt'. Python 3.* should allow the code to run without issues.

# Business Understanding
Airbnb, founded in 2008, has significantly disrupted the traditional hospitality industry through its innovative online marketplace model. At its core, Airbnb allows individuals to rent out their private spaces, such as homes, rooms, or unique accommodations, to guests from around the world. This concept not only expanded the range of lodging options for travelers but also empowered property owners to generate income from their unused spaces. Unlike conventional hotels, Airbnb's offerings are incredibly diverse, ranging from simple rooms to luxury villas, reflecting the varied preferences and budgets of travelers. This diversity has made Airbnb a popular choice for a wide range of customers, from budget backpackers to luxury vacationers.

What sets Airbnb apart is its use of technology to facilitate a seamless, user-friendly experience. The platform simplifies the process of listing, searching, and booking accommodations. Hosts can easily list their properties, set their prices, and manage bookings, while travelers can effortlessly search for and compare various lodging options. Additionally, Airbnb's review system, which allows both hosts and guests to rate and review each other, plays a crucial role in building trust and ensuring the quality of experiences. This peer-to-peer review system has been fundamental in promoting a sense of community and reliability, crucial in the sharing economy.

Moreover, Airbnb's impact extends beyond just the hospitality sector. It has become a significant player in the broader travel and tourism industry, offering 'Experiences' that allow locals to provide tours, classes, and unique activities to travelers. This aspect of Airbnb not only enriches the travel experience for guests but also provides additional income sources for local communities. By continuously innovating and expanding its services, Airbnb has not only changed how people travel but also how they interact with and experience new destinations, making it a pivotal player in the modern travel landscape.

# About Data

# 1) Calender.csv:
The data in "calendar_Seattle.csv" consists of the following columns:

listing_id: Identifier for the listing. /n
date: The date for the listing entry.
available: Indicates whether the listing is available on the given date ('t' for available, 'f' for not available).
price: The price of the listing for the given date.
