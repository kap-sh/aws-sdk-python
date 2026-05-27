# Getting Started

## Installation

```
pip install aws_sdk_s3
```

## Usage

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: call the abort_multipart_upload operation
        response = await s3.abort_multipart_upload()
        print(response["request_charged"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: paginate over list_buckets
        async for item in s3.iter_list_buckets():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks for the streaming parameter.

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: call put_object with a streaming request body
        async def chunks():
            yield b"Hello, World!"

        response = await s3.put_object(body=chunks())
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: call get_object and read the streaming response
        async with s3.get_object() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_` prefixed method.

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: wait for bucket_exists
        await s3.wait_bucket_exists(max_wait_time=300)
```

## Presigning

Some operations support presigning, which generates a URL that can be used without credentials. Use the `presigned_` prefixed method on the client to get a presigned URL.

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: get a presigned URL for delete_object
        url = s3.presigned_delete_object()
        print(url)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_s3 import AsyncS3Client
from aws_sdk_s3.error import NoSuchUpload


async def main():
    async with AsyncS3Client() as s3:
        try:
            await s3.abort_multipart_upload()
        except NoSuchUpload as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Default: 3 attempts for every operation
        response = await s3.abort_multipart_upload()

        # Override per operation
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 1})
```
