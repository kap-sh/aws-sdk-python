# Getting Started

## Installation

```
pip install capo-ivschat
```

## Usage

```python
from capo_ivschat import AsyncivschatClient


async def main():
    async with AsyncivschatClient() as s3:
        # Example: call the create_chat_token operation
        response = await s3.create_chat_token()
        print(response["token"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ivschat import AsyncivschatClient
from capo_ivschat.error import AccessDeniedException


async def main():
    async with AsyncivschatClient() as s3:
        try:
            await s3.create_chat_token()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ivschat import AsyncivschatClient


async def main():
    async with AsyncivschatClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.create_chat_token()

        # Override per operation
        response = await s3.create_chat_token(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.create_chat_token(config_overrides={"retry_max_attempts": 1})
```
