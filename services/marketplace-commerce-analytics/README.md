# Getting Started

## Installation

```
pip install aws-sdk-marketplace-commerce-analytics
```

## Usage

```python
from aws_sdk_marketplace_commerce_analytics import AsyncMarketplaceCommerceAnalyticsClient


async def main():
    async with AsyncMarketplaceCommerceAnalyticsClient() as s3:
        # Example: call the generate_data_set operation
        response = await s3.generate_data_set()
        print(response["data_set_request_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_marketplace_commerce_analytics import AsyncMarketplaceCommerceAnalyticsClient
from aws_sdk_marketplace_commerce_analytics.error import MarketplaceCommerceAnalyticsException


async def main():
    async with AsyncMarketplaceCommerceAnalyticsClient() as s3:
        try:
            await s3.generate_data_set()
        except MarketplaceCommerceAnalyticsException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_marketplace_commerce_analytics import AsyncMarketplaceCommerceAnalyticsClient


async def main():
    async with AsyncMarketplaceCommerceAnalyticsClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.generate_data_set()

        # Override per operation
        response = await s3.generate_data_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.generate_data_set(config_overrides={"retry_max_attempts": 1})
```
