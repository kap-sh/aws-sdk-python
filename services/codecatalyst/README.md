# Getting Started

## Installation

```
pip install capo-codecatalyst
```

## Usage

```python
from capo_codecatalyst import AsyncCodeCatalystClient


async def main():
    async with AsyncCodeCatalystClient() as s3:
        # Example: call the get_user_details operation
        response = await s3.get_user_details()
        print(response["user_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codecatalyst import AsyncCodeCatalystClient
from capo_codecatalyst.error import AccessDeniedException


async def main():
    async with AsyncCodeCatalystClient() as s3:
        try:
            await s3.get_user_details()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codecatalyst import AsyncCodeCatalystClient


async def main():
    async with AsyncCodeCatalystClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.get_user_details()

        # Override per operation
        response = await s3.get_user_details(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.get_user_details(config_overrides={"retry_max_attempts": 1})
```
