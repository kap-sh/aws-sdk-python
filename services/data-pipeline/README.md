# Getting Started

## Installation

```
pip install aws-sdk-data-pipeline
```

## Usage

```python
from aws_sdk_data_pipeline import AsyncDataPipelineClient


async def main():
    async with AsyncDataPipelineClient() as s3:
        # Example: call the activate_pipeline operation
        response = await s3.activate_pipeline()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_data_pipeline import AsyncDataPipelineClient


async def main():
    async with AsyncDataPipelineClient() as s3:
        # Example: paginate over describe_objects
        async for item in s3.iter_describe_objects():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_data_pipeline import AsyncDataPipelineClient
from aws_sdk_data_pipeline.error import InternalServiceError


async def main():
    async with AsyncDataPipelineClient() as s3:
        try:
            await s3.activate_pipeline()
        except InternalServiceError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_data_pipeline import AsyncDataPipelineClient


async def main():
    async with AsyncDataPipelineClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.activate_pipeline()

        # Override per operation
        response = await s3.activate_pipeline(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.activate_pipeline(config_overrides={"retry_max_attempts": 1})
```
