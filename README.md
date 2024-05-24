# Social Network Application

This Python program simulates a social network where users can sign up, follow each other, publish posts, like posts, comment on posts, and perform various other social interactions.

## Overview

The social network application consists of several classes:

- **users**: Represents users of the social network. Users can follow each other, publish posts, set status, etc.
- **Followers**: Represents followers of a user.
- **posts**: Represents posts published by users.
- **SocialNetwork**: Manages the social network including user sign-up, login, logout, etc.
- **postFactory**: Factory class to create different types of posts.

## Usage

- The program allows users to sign up with a unique username and password.
- Users can follow and unfollow each other.
- Users can publish three types of posts: Text, Image, and Sale.
- Users can like and comment on posts.
- Sale posts can have a price and location associated with them.
- Users can discount the price of their sale posts and mark them as sold.

## Run
run main.py

## Tests

-run auto_check.py expected to see succses message
-test_output.txt, main_test.py expected to see main_test output as test_output
