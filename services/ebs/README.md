# Getting Started

## Installation

```
pip install aws-sdk-ebs
```

## Usage

```python
from aws_sdk_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as s3:
        # Example: call the complete_snapshot operation
        response = await s3.complete_snapshot()
        print(response["status"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks for the streaming parameter.

```python
from aws_sdk_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as s3:
        # Example: call put_snapshot_block with a streaming request body
        async def chunks():
            yield b"Hello, World!"

        response = await s3.put_snapshot_block(block_data=chunks())
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from aws_sdk_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as s3:
        # Example: call get_snapshot_block and read the streaming response
        async with s3.get_snapshot_block() as response:
            async for chunk in response["block_data"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_ebs import AsyncEBSClient
from aws_sdk_ebs.error import AccessDeniedException


async def main():
    async with AsyncEBSClient() as s3:
        try:
            await s3.complete_snapshot()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.complete_snapshot()

        # Override per operation
        response = await s3.complete_snapshot(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.complete_snapshot(config_overrides={"retry_max_attempts": 1})
```
