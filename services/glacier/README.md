# Getting Started

## Installation

```
pip install aws-sdk-glacier
```

## Usage

```python
from aws_sdk_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as s3:
        # Example: call the abort_multipart_upload operation
        response = await s3.abort_multipart_upload()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as s3:
        # Example: paginate over list_jobs
        async for item in s3.iter_list_jobs():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

```python
from aws_sdk_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as s3:
        # Example: call upload_archive with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await s3.upload_archive(body=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await s3.upload_archive(body=b'Hello, World!')
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from aws_sdk_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as s3:
        # Example: call get_job_output and read the streaming response
        async with s3.get_job_output() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_` prefixed method.

```python
from aws_sdk_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as s3:
        # Example: wait for vault_exists
        await s3.wait_vault_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_glacier import AsyncGlacierClient
from aws_sdk_glacier.error import InvalidParameterValueException


async def main():
    async with AsyncGlacierClient() as s3:
        try:
            await s3.abort_multipart_upload()
        except InvalidParameterValueException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.abort_multipart_upload()

        # Override per operation
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 1})
```
