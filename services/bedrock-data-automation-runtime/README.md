# Getting Started

## Installation

```
pip install capo-bedrock-data-automation-runtime
```

## Usage

```python
from capo_bedrock_data_automation_runtime import AsyncBedrockDataAutomationRuntimeClient


async def main():
    async with AsyncBedrockDataAutomationRuntimeClient() as s3:
        # Example: call the invoke_data_automation operation
        response = await s3.invoke_data_automation()
        print(response["output_configuration"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_data_automation_runtime import AsyncBedrockDataAutomationRuntimeClient
from capo_bedrock_data_automation_runtime.error import AccessDeniedException


async def main():
    async with AsyncBedrockDataAutomationRuntimeClient() as s3:
        try:
            await s3.invoke_data_automation()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_data_automation_runtime import AsyncBedrockDataAutomationRuntimeClient


async def main():
    async with AsyncBedrockDataAutomationRuntimeClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.invoke_data_automation()

        # Override per operation
        response = await s3.invoke_data_automation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.invoke_data_automation(config_overrides={"retry_max_attempts": 1})
```
