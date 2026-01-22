# Test-Driven Development Kata Project
## This is my complete implementation from the starter template project found at [Python TDD Kata Starter](https://github.com/btgrant-76/python-tdd-kata-starter)
- [x] Completed TDD Kata 1 [Instructions](https://osherove.com/tdd-kata-1/)

## Introductory Reading
These are short. You should read them; I'll wait:
- [Kata - the Only Way to Learn TDD](http://www.peterprovost.org/blog/2012/05/02/kata-the-only-way-to-learn-tdd/)  The author lists a number of TDD katas in addition to discussing the practice.
- [Uncle Bob's "Three Rules of TDD"](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)
- [TDD Test-driven development cycle from Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle) for another perspective on the "Three Rules"

## What's in This Project
The project features a minimal setup to allow you to quickly start practicing TDD katas using Python and [`pytest`](https://docs.pytest.org/). 

- `reqiurements.txt`:  Install the project's requirements/dependencies with `pip install -r requirements.txt`.
- `pytest.ini`:  This configuration tells `pytest` where to find both source and test files so.
- `src/string_calculator.py` and `test/string_calculator_test.py`:  Starter files for the [String Calculator kata](https://osherove.com/tdd-kata-1/)
  
### Commands
All of these commands can be run at the root of the project.
- `pytest`:  run all tests
- `pytest --cov=src`:  run all tests and produce a test coverage report. This is certainly not necessary for learning TDD, but it can be interesting to understand how complete your unit tests are.
- `ptw`:  starts [pytest-watch](https://pypi.org/project/pytest-watch/) which will automatically run all tests any time a file in the project has changed. While this is not necessary for learning TDD, I have found that tools like this add to the enjoyment of practicing TDD. 