# Contributing

### **Table of Contents**

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Standards and Guidelines](#standards-and-guidelines)
  - [Theme Guidelines](#theme-guidelines)
  - [Language Guidelines](#language-guidelines)
  - [Quote Guidelines](#quote-guidelines)
- [Questions](#questions)

## Getting Started

When contributing to vinyl, it's good to know our best practices, tips, and tricks. First, Vinyl (Server) is written in Python thus, we assume you are comfortable in Python or have basic knowledge of them. We use FastAPI for the webserver, Redis as the database.

We are planning to containerize the entire application using Docker. 

## Installation

1. Fork and Clone the repo
   ```sh
   git clone https://github.com/radioactive11/vinyl-server.git
   ```
2. Create and activate virtual environment
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the requirements
   ```sh
   python3 -m pip install -r requirements.txt
   ```
4. Set PYTHONPATH environment variable
   ```sh
   export PYTHONPATH=app
   ```
5. Start the server
```sh
uvicorn main:app
```

6. Start Redis server (on port 6379)
```sh
redis-server
```



## Standards and Guidelines

Below are a set of general guidelines for different types of changes.

### Language Guidelines

- Do not include swear words
- Ensure you use a formatter (like Black)
- Make sure your code follows the PEP-8 guidelines


## Questions

If you have any questions, comments, concerns, or problems let me know on [GitHub](https://github.com/radioactive11) or ask a question on vinyl's [GitHub discussions](https://github.com/radioactive11/vinyl/discussions) and a contributor will be happy to assist you.