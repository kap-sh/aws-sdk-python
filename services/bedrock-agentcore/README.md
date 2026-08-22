# Getting Started

## Installation

```
pip install capo-bedrock-agentcore
```

## Usage

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        # Example: call the complete_resource_token_auth operation
        response = await bedrock_agent_core.complete_resource_token_auth()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient
from capo_bedrock_agentcore.error import AccessDeniedException


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        try:
            await bedrock_agent_core.complete_resource_token_auth()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        # Default: 3 attempts for every operation
        response = await bedrock_agent_core.complete_resource_token_auth()

        # Override per operation
        response = await bedrock_agent_core.complete_resource_token_auth(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_agent_core.complete_resource_token_auth(config_overrides={"retry_max_attempts": 1})
```
