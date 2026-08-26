
# capo (caporegime)

Community-driven AWS SDK for Python. Manage AWS services like a [capo](https://en.wikipedia.org/wiki/Caporegime).

## Features

- **async and sync** — Use the same API for both async and sync code, with support for asyncio and [trio](https://trio.readthedocs.io).
- **WASM support** — Runs in WASM environments via [Pyodide](https://pyodide.org).
- **typed and documented** — Fully typed and documented for a better developer experience.
- **simple inputs** — No need to import separate parameter classes; nested inputs are fully typed via [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).
- **generated from Smithy models** — The SDK is generated from the official [Smithy](https://smithy.io) models describing AWS APIs, ensuring accuracy and consistency.
- **zero runtime overhead** — Codegen produces dedicated serialization and deserialization code for each operation, avoiding reflection.
- **interchangeable input/output** — Input and output types use the same [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), so you can pass a response directly as input when appropriate.
- **built on [zapros](https://zapros.dev)** — A modern HTTP client for Python that abstracts HTTP semantics from the transport implementation.
- **fast to import** — import time stays flat even for huge services like EC2.
- **interceptors** — Hook into the operation request/response lifecycle to inspect, log, or modify calls.

> **Warning**
> The API should be mostly stable, but some breaking changes may occur as the SDK is still in early development. We strongly recommend pinning the version before the first major release.

## Installation

Every service is a standalone package, so you only install the ones you actually use. Packages are published under the `capo-` prefix:

```bash
uv add capo-ec2                        # Amazon EC2 (also covers Amazon VPC)
uv add capo-s3                         # Amazon S3
uv add capo-iam                        # AWS IAM
uv add capo-rds                        # Amazon RDS
uv add capo-lambda                     # AWS Lambda
uv add capo-cloudwatch                 # Amazon CloudWatch
uv add capo-elastic-load-balancing     # Elastic Load Balancing (ELB)
uv add capo-route-53                   # Amazon Route 53
uv add capo-cloudfront                 # Amazon CloudFront
```

Note that Amazon VPC has no separate package — its API is part of EC2, so `capo-ec2` covers it.

### Services not yet on PyPI

Not every service is on PyPI yet. We publish incrementally because of PyPI's limits on new projects and total upload size. If the service you need isn't published, please [open an issue](https://github.com/kap-sh/capo/issues) so we can prioritize publishing it.



## Async/Sync Usage

All the services have both async and sync client. The async client is simply prefixed with `Async` (e.g. `AsyncS3Client`).

```python
from capo_s3 import AsyncS3Client

async def main():
    async with AsyncS3Client() as s3:
        response = await s3.create_bucket("capo")
        print(response)
```

Sync usage is the same, just without the `Async` prefix and without `await`:

```python
from capo_s3 import S3Client

with S3Client() as s3:
    response = s3.create_bucket("capo")
    print(response)
```

## Input/Output Types

No matter how nested the input types are, you don't need to import any additional classes. All input and output types are fully typed via [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).

```python
from capo_s3 import AsyncS3Client

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
from capo_s3 import AsyncS3Client
from capo_s3.errors import NoSuchUpload


async with AsyncS3Client() as s3:
    try:
        await s3.abort_multipart_upload()
    except NoSuchUpload as e:
        print(f"Error: {e}")
        print(e.data)  # additional error data
```

Note that the service errors (errors returned by AWS) might have additional data of any shape stored in the `data` attribute, which is a TypedDict. You can access it to get more information about the error.

All the service errors that an operation can raise are documented in that operation method's docstring.

## Streaming

If the operation's input is a streaming blob, you can pass any `AsyncIterator[bytes]` or just a `bytes` object.

```python
from capo_s3 import AsyncS3Client

s3_client = AsyncS3Client()

response = await s3_client.put_object("bucket_name", "key", body=b"some binary data")
```

Or, if you don't want to load the entire blob into memory, you can pass an `AsyncIterator[bytes]`:

```python
from capo_s3 import AsyncS3Client

async def async_iterator():
    yield b"capo"

response = await s3_client.put_object("bucket_name", "key", body=async_iterator(), content_length=4)
```

As you might have noticed, we also passed the `content_length`. That's an AWS requirement when using streaming inputs; it must always know the length of the blob before sending it to AWS.

Note that the stream can be any iterator of bytes; it need not be the file's content. You can stream any data you want, for example, directly from the HTTP response of another service, or from a database, etc.

The catch with a plain iterator is that it can be sent only once. If the request fails after the body was transmitted (a throttling error, a dropped connection), there is nothing left to resend, so the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client) stream a file from disk and take the `content_length` from the file size, so you don't need to pass it:

```python
from capo_s3 import AsyncS3Client, Body

s3_client = AsyncS3Client()

response = await s3_client.put_object("bucket_name", "key", body=Body.async_from_path("data.bin"))
```

For sources other than files, build a `Body` from an *opener* — a context manager that yields a `(stream, length)` pair each time it is entered. The SDK enters it before every attempt and exits it when the operation finishes:

```python
from contextlib import asynccontextmanager

from capo_s3 import AsyncS3Client, Body

@asynccontextmanager
async def open_rows():
    rows = await db.fetch_all()  # re-read from your data source on every attempt

    async def chunks():
        for row in rows:
            yield row

    yield chunks(), sum(len(row) for row in rows)

response = await s3_client.put_object("bucket_name", "key", body=Body(open_rows))
```

The output as mentioned before also can be a stream, in such case, the operation will return a context manager that yield the response, ensuring that the resource is properly closed after the response is consumed.

```python
from capo_s3 import AsyncS3Client

s3_client = AsyncS3Client()

async with s3_client.get_object("bucket_name", "key") as response:
    async for chunk in response["body"]:
        print(chunk)
```

The event streaming operations are similar, but instead of using `AsyncIterator[bytes]`, they use `AsyncIterator[Event]`, where `Event` is a TypedDict that represents the event type.

```python
from capo_s3 import AsyncS3Client

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

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_s3 import AsyncS3Client


async with AsyncS3Client() as s3:
    # Example: wait for bucket_exists
    await s3.wait_until_bucket_exists(max_wait_time=300)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3 import AsyncS3Client


async with AsyncS3Client() as s3:
    # Example: paginate over list_buckets
    async for item in s3.iter_list_buckets():
        print(item)
```

## Presigning

Some operations support presigning, which generates a URL that can be used without credentials. Use the `presigned_` prefixed method on the client to get a presigned URL.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: get a presigned URL for delete_object
        url = s3.presigned_delete_object()
        print(url)
```

> **Note**
> Smithy models don't indicate which operations support presigning, so presigned methods are added by maintainers rather than the code generator. If you notice an operation that should support presigning but has no `presigned_` method, please [open an issue](https://github.com/kap-sh/capo/issues).

## Interceptors

Interceptors let you hook into the operation lifecycle. An operation interceptor receives the operation request and a `next` callable that invokes the rest of the chain, returning the operation response. You can inspect or modify the request before calling `next`, and inspect or modify the response after.

```python
import asyncio
from typing import Any, Awaitable, Callable

from capo_s3 import AsyncOperationRequest, AsyncOperationResponse, AsyncS3Client


async def debug_interceptor(
    request: AsyncOperationRequest[Any],
    next: Callable[[AsyncOperationRequest[Any]], Awaitable[AsyncOperationResponse]],
):
    print(request)
    response = await next(request)
    print(response)
    return response


async def main():
    async with AsyncS3Client(operation_interceptors=[debug_interceptor]) as client:
        async for item in client.iter_list_buckets():
            print(item)


asyncio.run(main())
```

> **Note**
> An `operation_interceptor` sits between the operation request and the operation response — not at the HTTP layer. For HTTP-level interceptors/middlewares, see the [Configuring the HTTP client](#configuring-the-http-client) section below.

## Configuring the HTTP client

The SDK is built on [zapros](https://zapros.dev). You can pass your own HTTP handler via the `http_handler` argument, including any zapros middleware wrapping a network handler. This is the right place for HTTP-level concerns such as caching, mocks, or custom transports. See the [zapros handlers documentation](https://zapros.dev/handlers) for the available handlers and middlewares.

```python
import asyncio

from zapros import AsyncStdNetworkHandler, CacheMiddleware

from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client(
        http_handler=CacheMiddleware(AsyncStdNetworkHandler())
    ) as client:
        async for item in client.iter_list_buckets():
            print(item)


asyncio.run(main())
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Default: 3 attempts for every operation
        response = await s3.abort_multipart_upload()

        # Override per operation
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 1})
```