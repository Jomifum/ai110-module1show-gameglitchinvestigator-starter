# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Decimal "3.7" | "Generate pytest cases for parse_guess covering edge-case inputs... a decimal string '3.7' should return ok=True with value 3" | test_decimal_string_truncates_to_int | Yes | parse_guess uses int(float(raw)), so I wanted to confirm decimals truncate to an int predictably instead of crashing. |
| Negative "-5" | (same prompt, covering all cases at once) | test_negative_number_is_parsed | Yes | Tests an out-of-range but technically valid integer to ensure parsing itself doesn't fail. |
| Non-numeric "abc" | (same prompt) | test_non_numeric_string_returns_error | Yes | Confirms the function returns ok=False with an error message rather than throwing an exception. |
| Empty "" | (same prompt) | test_empty_string_returns_error | Yes | A common accidental input that should be handled gracefully. |
| Large "999999999" | (same prompt) | test_extremely_large_number_parses_without_crashing | Yes | Verifies very large but valid integers parse without overflow or crashing. |

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
