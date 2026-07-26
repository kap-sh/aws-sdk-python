# Getting Started

## Installation

```
pip install capo-resource-groups-tagging-api
```

## Usage

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as s3:
        # Example: call the describe_report_creation operation
        response = await s3.describe_report_creation()
        print(response["status"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as s3:
        # Example: paginate over get_compliance_summary
        async for item in s3.iter_get_compliance_summary():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient
from capo_resource_groups_tagging_api.error import ConstraintViolationException


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as s3:
        try:
            await s3.describe_report_creation()
        except ConstraintViolationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.describe_report_creation()

        # Override per operation
        response = await s3.describe_report_creation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.describe_report_creation(config_overrides={"retry_max_attempts": 1})
```
