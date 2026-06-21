
# aws-sdk-python

Modern AWS SDK for Python — async-native, fully typed, and generated from official Smithy models.

## Features

- **async and sync** — Use the same API for both async and sync code, with support for asyncio and [trio](https://trio.readthedocs.io).
- **WASM support** — Runs in WASM environments via [Pyodide](https://pyodide.org).
- **typed and documented** — Fully typed and documented for a better developer experience.
- **simple inputs** — No need to import separate parameter classes; nested inputs are fully typed via [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).
- **generated from Smithy models** — The SDK is generated from the official [Smithy](https://smithy.io) models describing AWS APIs, ensuring accuracy and consistency.
- **zero runtime overhead** — Codegen produces dedicated serialization and deserialization code for each operation, avoiding reflection.
- **interchangeable input/output** — Input and output types use the same [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), so you can pass a response directly as input when appropriate.
- **built on [zapros](https://zapros.dev)** — A modern HTTP client for Python that abstracts HTTP semantics from the transport implementation.

> **Warning**
> The API should be mostly stable, but some breaking changes may occur as the SDK is still in early development. We strongly recommend pinning the version before the first major release.

## Installation

This repository ships standalone packages for each service.

For now, we don't have all the packages published to PyPi, we'll do that once we figure out the best way to distribute them without violating https://aws.amazon.com/trademark-guidelines/, and under which namespace we should publish them. For now, you can install the packages directly from GitHub:

```bash
uv add git+https://github.com/kap-sh/aws-sdk-python#subdirectory=services/s3
# or any other services, for example:
uv add git+https://github.com/kap-sh/aws-sdk-python#subdirectory=services/ec2
uv add git+https://github.com/kap-sh/aws-sdk-python#subdirectory=services/dynamodb
```



## Async/Sync Usage

All the services have both async and sync client. The async client is simply prefixed with `Async` (e.g. `AsyncS3Client`).

```python
from aws_sdk_s3 import AsyncS3Client

async def main():
    async with AsyncS3Client() as s3:
        response = await s3.create_bucket("capo")
        print(response)
```

Sync usage is the same, just without the `Async` prefix and without `await`:

```python
from aws_sdk_s3 import S3Client

with S3Client() as s3:
    response = s3.create_bucket("capo")
    print(response)
```

## Input/Output Types

No matter how nested the input types are, you don't need to import any additional classes. All input and output types are fully typed via [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).

```python
from aws_sdk_s3 import AsyncS3Client

async with AsyncS3Client() as s3_client:
    response = await s3_client.create_bucket(
        bucket="some_bucket",
        create_bucket_configuration={
            "location": {
                "name": "location_name"
            }
        }
    )

print(response["location"])
```

The output types are also TypeDicts, we do this to make the input/output types interchangeable. You can pass the output member to another operation that accepts the same type as input.

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_s3 import AsyncS3Client
from aws_sdk_s3.error import NoSuchUpload


async with AsyncS3Client() as s3:
    try:
        await s3.abort_multipart_upload()
    except NoSuchUpload as e:
        print(f"Error: {e}")
        print(e.data)  # additional error data
```

Note that the service errors (errors returned by AWS) might have additional data of any shape stored in the `data` attribute, which is a TypedDict. You can access it to get more information about the error.

## Streaming

If the operation's input is a streaming blob, you can pass any `AsyncIterator[bytes]` or just a `bytes` object.

```python
from aws_sdk_s3 import AsyncS3Client

s3_client = AsyncS3Client()

response = await s3_client.put_object("bucket_name", "key", body=b"some binary data")
```

Or, if you don't want to load the entire blob into memory, you can pass an `AsyncIterator[bytes]`:

```python
from aws_sdk_s3 import AsyncS3Client

async def async_iterator():
    yield b"capo"

response = await s3_client.put_object("bucket_name", "key", body=async_iterator(), content_length=4)
```

As you might have noticed, we also passed the `content_length`. That's an AWS requirement when using streaming inputs; it must always know the length of the blob before sending it to AWS.

Note that the stream can be any iterator of bytes; it need not be the file's content. You can stream any data you want, for example, directly from the HTTP response of another service, or from a database, etc.

The output as mentioned before also can be a stream, in such case, the operation will return a context manager that yield the response, ensuring that the resource is properly closed after the response is consumed.

```python
from aws_sdk_s3 import AsyncS3Client

s3_client = AsyncS3Client()

async with s3_client.get_object("bucket_name", "key") as response:
    async for chunk in response["body"]:
        print(chunk)
```

The event streaming operations are similar, but instead of using `AsyncIterator[bytes]`, they use `AsyncIterator[Event]`, where `Event` is a TypedDict that represents the event type.

```python
from aws_sdk_s3 import AsyncS3Client

s3_client = AsyncS3Client()


async def main():
    async with s3_client.select_object_content(
        "bucket_name",
        "key",
        expression="SELECT * FROM S3Object s WHERE s._1 > 100",
        expression_type="SQL",
        input_serialization={
            "csv": {"file_header_info": "NONE"},
            "compression_type": "NONE",
        },
        output_serialization={"csv": {}},
    ) as response:
        async for event in response["payload"]:
            if "End" in event:
                print(event["End"])
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_` prefixed method.

```python
from aws_sdk_s3 import AsyncS3Client


async with AsyncS3Client() as s3:
    # Example: wait for bucket_exists
    await s3.wait_bucket_exists(max_wait_time=300)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_s3 import AsyncS3Client


async with AsyncS3Client() as s3:
    # Example: paginate over list_buckets
    async for item in s3.iter_list_buckets():
        print(item)
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