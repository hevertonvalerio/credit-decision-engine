# Credit Decision Engine

A credit decision engine that evaluates the potential of real estate customers.

## The problem

### The business problem
Closing a deal is great, but what happens when you aren't sure if it will be paid? That's why credit analysis is so important, it evaluates client credibility, payment capacity, and guarantee offered.

The company has to manage customers guarantees, which type, and if the amount will be sufficient, so it is necessary to make a credit evaluation of this client. 

Notice that this is a very complex task, involving many parameters, some numeric, others categorical. 

### The current proposal to resolve
An LLM performs every part of the evaluation.

### Why doesn't it work
Why can't we use LLMs alone to decide credit evaluation? 

- Non-deterministic (we can't repeat exactly the same flow)
- Untraceable (this creates legal exposure, we can't guarantee an equal evaluation)
- Unexplainable (the decision flow of an LLM can't be audited adequately)
- Expensive, false economy (the token cost isn't worth its benefits)

## How this project aims to resolve it
This project builds a Machine Learning model to mitigate all of these problems.

## Status
Foundation only: packaging, tests and linting are in place. No domain logic yet.

## Getting started

### Requirements
- Python 3.11 or newer
- git

### Setup
Clone the repository:

```bash
git clone https://github.com/hevertonvalerio/credit-decision-engine.git
cd credit-decision-engine
```

Create and activate a virtual environment:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

```powershell
# Windows (PowerShell)
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the package with its development dependencies:

```bash
pip install -e ".[dev]"
```

### Verify the installation
```bash
pytest
ruff check
```

Both commands should pass with no errors.