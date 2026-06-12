# Getting Started

## Installation

```
pip install aws-sdk-migrationhubstrategy
```

## Usage

```python
from aws_sdk_migrationhubstrategy import AsyncMigrationHubStrategyClient


async def main():
    async with AsyncMigrationHubStrategyClient() as s3:
        # Example: call the get_application_component_details operation
        response = await s3.get_application_component_details()
        print(response["application_component_detail"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_migrationhubstrategy import AsyncMigrationHubStrategyClient


async def main():
    async with AsyncMigrationHubStrategyClient() as s3:
        # Example: paginate over get_server_details
        async for item in s3.iter_get_server_details():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_migrationhubstrategy import AsyncMigrationHubStrategyClient
from aws_sdk_migrationhubstrategy.error import InternalServerException


async def main():
    async with AsyncMigrationHubStrategyClient() as s3:
        try:
            await s3.get_application_component_details()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_migrationhubstrategy import AsyncMigrationHubStrategyClient


async def main():
    async with AsyncMigrationHubStrategyClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.get_application_component_details()

        # Override per operation
        response = await s3.get_application_component_details(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.get_application_component_details(config_overrides={"retry_max_attempts": 1})
```
