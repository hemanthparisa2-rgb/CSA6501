def create_prompt(module, strategy, task, examples=""):

    if strategy == "Zero-Shot":

        prompt = f"""
You are PromptCraft, a professional engineering assistant.

MODULE:
{module}

TASK:
{task}

Instructions:
1. Understand the engineering problem.
2. Provide a technically correct solution.
3. Explain the important concepts.
4. Provide code when required.
5. Keep the answer clear and practical.
"""

    elif strategy == "Few-Shot":

        prompt = f"""
You are PromptCraft, a professional engineering assistant.

MODULE:
{module}

EXAMPLES:
{examples}

NEW TASK:
{task}

Instructions:
1. Study the examples.
2. Follow their response structure.
3. Apply the same pattern to the new task.
4. Provide a clear and technically useful answer.
"""

    elif strategy == "Structured Reasoning":

        prompt = f"""
You are PromptCraft, an expert software engineering assistant.

MODULE:
{module}

TASK:
{task}

Analyze the task systematically and provide the response using:

1. Problem Understanding
2. Key Issues
3. Proposed Solution
4. Implementation / Example
5. Final Answer

Do not provide private chain-of-thought.
Provide only a concise reasoning summary and final answer.
"""

    return prompt.strip()