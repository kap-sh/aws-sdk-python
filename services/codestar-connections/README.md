# Getting Started

## Installation

```
pip install aws-sdk-codestar-connections
```

## Usage

```python
from aws_sdk_codestar_connections import AsyncCodeStarconnectionsClient


async def main():
    async with AsyncCodeStarconnectionsClient() as s3:
        # Example: call the create_connection operation
        response = await s3.create_connection()
        print(response["connection_arn"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_codestar_connections import AsyncCodeStarconnectionsClient
from aws_sdk_codestar_connections.error import LimitExceededException


async def main():
    async with AsyncCodeStarconnectionsClient() as s3:
        try:
            await s3.create_connection()
        except LimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_codestar_connections import AsyncCodeStarconnectionsClient


async def main():
    async with AsyncCodeStarconnectionsClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.create_connection()

        # Override per operation
        response = await s3.create_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.create_connection(config_overrides={"retry_max_attempts": 1})
```
