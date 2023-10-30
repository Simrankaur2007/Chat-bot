# SDF Assignment 5

## Description
This assignment uses several functions working together to produce chatbot banking functionality.  Several functions 
are created and unit tested and once all unit testing is 
complete, the functions are integrated into a single application.

## Author
ACE Faculty

## Revised by
{Simran Kaur}



# Reflection:
## 1. Identify any challenges or issues you encountered while writing your functions.
#### During the process of writing the functions for the chatbot application, the encountered several challenges and issues are:

- Ensuring proper error handling: Writing functions that handle various types of errors, such as invalid inputs or missing data, required careful consideration. Error handling is crucial to make the chatbot user-friendly and robust.

- Mocking user input for unit tests: Writing unit tests that involve user input can be a bit challenging. Using the unittest.mock library to simulate user input during testing helped address this issue.

- Coordinating function interactions: Coordinating the interactions between different functions, such as get_account, get_amount, get_balance, and make_deposit, within the chatbot function required careful planning and handling of data flow.

- Ensuring code readability and maintainability: Writing clean and maintainable code is essential for the long-term viability of the application. This involved writing clear docstrings, using meaningful variable names, and structuring the code logically.

## 2. Discuss the benefits and challenges of developing and using unit tests.
#### Benefits:
- Early Detection of Issues: Unit tests allow for the early detection and debugging of code issues, which can prevent more significant problems down the line.

- Improved Code Quality: Writing tests forces developers to think critically about their code, leading to higher code quality.

- Documentation: Tests serve as documentation, providing clear examples of how functions should be used and what they are expected to return.

- Confidence in Code Changes: With a comprehensive set of unit tests, developers can make changes or optimizations to their code with confidence, knowing that the tests will catch regressions.

- Collaboration: Tests make it easier for multiple developers to work on a codebase, as they can independently verify that their changes haven't broken existing functionality.

#### Challenges:
- Test Writing Overhead: Writing tests can be time-consuming, especially for complex functions. This overhead can be a challenge when working on tight deadlines.

- Test Maintenance: Tests need to be updated when code changes, which can be a maintenance burden. However, this is a small price to pay for the benefits they provide.

- Coverage: Achieving full test coverage, especially for large codebases, can be challenging. It's essential to strike a balance between covering critical functionality and avoiding excessive testing.

- Test Data: Generating test data, especially for edge cases, can be challenging and may require additional code to set up test scenarios.