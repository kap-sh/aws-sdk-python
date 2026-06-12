# Getting Started

## Installation

```
pip install aws-sdk-apigatewaymanagementapi
```

## Usage

```python
from aws_sdk_apigatewaymanagementapi import AsyncApiGatewayManagementApiClient


async def main():
    async with AsyncApiGatewayManagementApiClient() as s3:
        # Example: call the delete_connection operation
        response = await s3.delete_connection()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_apigatewaymanagementapi import AsyncApiGatewayManagementApiClient
from aws_sdk_apigatewaymanagementapi.error import ForbiddenException


async def main():
    async with AsyncApiGatewayManagementApiClient() as s3:
        try:
            await s3.delete_connection()
        except ForbiddenException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_apigatewaymanagementapi import AsyncApiGatewayManagementApiClient


async def main():
    async with AsyncApiGatewayManagementApiClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.delete_connection()

        # Override per operation
        response = await s3.delete_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.delete_connection(config_overrides={"retry_max_attempts": 1})
```
