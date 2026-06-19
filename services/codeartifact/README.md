# Getting Started

## Installation

```
pip install aws-sdk-codeartifact
```

## Usage

```python
from aws_sdk_codeartifact import AsynccodeartifactClient


async def main():
    async with AsynccodeartifactClient() as s3:
        # Example: call the associate_external_connection operation
        response = await s3.associate_external_connection()
        print(response["repository"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_codeartifact import AsynccodeartifactClient


async def main():
    async with AsynccodeartifactClient() as s3:
        # Example: paginate over list_allowed_repositories_for_group
        async for item in s3.iter_list_allowed_repositories_for_group():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

```python
from aws_sdk_codeartifact import AsynccodeartifactClient


async def main():
    async with AsynccodeartifactClient() as s3:
        # Example: call publish_package_version with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await s3.publish_package_version(asset_content=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await s3.publish_package_version(asset_content=b'Hello, World!')
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from aws_sdk_codeartifact import AsynccodeartifactClient


async def main():
    async with AsynccodeartifactClient() as s3:
        # Example: call get_package_version_asset and read the streaming response
        async with s3.get_package_version_asset() as response:
            async for chunk in response["asset"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_codeartifact import AsynccodeartifactClient
from aws_sdk_codeartifact.error import AccessDeniedException


async def main():
    async with AsynccodeartifactClient() as s3:
        try:
            await s3.associate_external_connection()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_codeartifact import AsynccodeartifactClient


async def main():
    async with AsynccodeartifactClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.associate_external_connection()

        # Override per operation
        response = await s3.associate_external_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.associate_external_connection(config_overrides={"retry_max_attempts": 1})
```
