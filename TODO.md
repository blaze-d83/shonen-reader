# TODO List 
---

## Project Setup

- [x] Install Django and create a new project

- [x] Set up PostgreSQL database configuration

- [x] Initialize a Git repository and create a `.gitignore` file

---

## User Authentication

- [] Set up Django's built-in authentication system

      - [ ] Create a custom user model to include username and avatar

      - [ ] Implement user registration with email, password, username, and avatar

      - [ ] Implement user login functionality

- [x] Create the admin login redirect to the admin URL (`/admin`)

      - [x] Set up a separate login page for admins

      - [x] Implement URL routing to redirect to admin dashboard upon successful login

---

## Admin Dashboard

- [x] Set up a basic admin dashboard

      - [x] Use Django admin or create a custom dashboard interface

      - [ ] Implement a nested list of mangas and their chapters

- [x] Create forms for adding new mangas and chapters

      - [x] Form for adding new manga with fields: title, description, release date

      - [x] Form for adding new chapter with fields: title, description, release date, ordered image uploads

- [x] Implement image upload handling for manga chapters

---

## Client Application

- [ ] Set up a React front-end for the client application

      - [ ] Create a React project and configure it to work with Django backend

      - [ ] Set up routing for client application pages

- [ ] Implement pages for:

      - [ ] Viewing manga list

      - [ ] Viewing manga details

      - [ ] Viewing and reading manga chapters

- [ ] Implement navigation:

      - [ ] Navigation through manga pages

      - [ ] Reader with left and right arrows to navigate chapters

- [ ] Implement like/dislike functionality

      - [ ] Backend: API endpoints for liking/disliking

      - [ ] Frontend: Like/dislike buttons and handling user interactions

- [ ] Implement nested comments

      - [ ] Backend: API endpoints for adding, editing, and deleting comments

      - [ ] Frontend: Display nested comments and forms for posting comments

---

## Media Management

- [ ] Brainstorm and plan media management strategies

      - [ ] Decide on storage solution for images (e.g., local storage, cloud storage)

      - [ ] Implement media upload, retrieval, and display functionalities

---

## Future Enhancements

- [ ] Implement version control for manga and chapters

- [ ] Add search and filtering functionalities

      - [ ] Backend: API endpoints for search and filtering

      - [ ] Frontend: Search bar and filtering options

- [ ] Add notification system

      - [ ] Backend: Set up notifications for new content and updates

      - [ ] Frontend: Display notifications to users

- [ ] Add data visualization for admin dashboard

      - [ ] Charts and graphs for likes and comments metrics

- [ ] Implement tools for managing user comments and spam protection

      - [ ] Reporting system for inappropriate comments

      - [ ] Moderation tools for admin

---

## Testing and Iteration

- [ ] Write unit tests for backend functionalities

- [ ] Write integration tests for client application

- [ ] Perform user testing and gather feedback

- [ ] Iterate on the application based on feedback and testing results

---

## Scalability and Performance

- [ ] Plan and implement scalability solutions

      - [ ] Optimize database queries and application performance

      - [ ] Set up caching and load balancing solutions

---

## Documentation

- [ ] Write user documentation for registration, login, and usage

- [ ] Write developer documentation for setup, development, and deployment

- [ ] Maintain a changelog for future updates and enhancements




