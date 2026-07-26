# Getting Started

## Installation

```
pip install capo-workmailmessageflow
```

## Usage

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient


async def main():
    async with AsyncWorkMailMessageFlowClient() as s3:
        # Example: call the get_raw_message_content operation
        response = await s3.get_raw_message_content()
        print(response["message_content"])
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient


async def main():
    async with AsyncWorkMailMessageFlowClient() as s3:
        # Example: call get_raw_message_content and read the streaming response
        async with s3.get_raw_message_content() as response:
            async for chunk in response["message_content"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient
from capo_workmailmessageflow.error import ResourceNotFoundException


async def main():
    async with AsyncWorkMailMessageFlowClient() as s3:
        try:
            await s3.get_raw_message_content()
        except ResourceNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient


async def main():
    async with AsyncWorkMailMessageFlowClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.get_raw_message_content()

        # Override per operation
        response = await s3.get_raw_message_content(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.get_raw_message_content(config_overrides={"retry_max_attempts": 1})
```
