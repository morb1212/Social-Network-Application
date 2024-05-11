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
## Tests

### User Management Test

- **Objective**: Verify that user-related functionalities work correctly.
- **Steps**:
  1. Create new users with unique usernames and passwords.
  2. Ensure that users can log in and log out successfully.
  3. Test user follow and unfollow actions, checking that the follower count and following list are updated accordingly.

### Post Management Test

- **Objective**: Validate the creation and interaction with posts.
- **Steps**:
  1. Create different types of posts (text, image, sale) by various users.
  2. Test post publication and retrieval, ensuring that posts are displayed correctly.
  3. Like and comment on posts, verifying that likes and comments are recorded and displayed accurately.
  4. Test discounting and marking sale posts as sold, ensuring that the price and status are updated accordingly.

### Social Network Integration Test

- **Objective**: Ensure that the entire social network application functions correctly.
- **Steps**:
  1. Perform end-to-end testing of user sign-up, login, post creation, interaction, and logout functionalities.
  2. Simulate user interactions such as following/unfollowing other users, liking posts, and commenting on posts.
  3. Verify that the social network maintains consistent user data, post data, and interaction records.

