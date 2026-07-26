# Getting Started

## Installation

```
pip install capo-marketplace-entitlement-service
```

## Usage

```python
from capo_marketplace_entitlement_service import AsyncMarketplaceEntitlementServiceClient


async def main():
    async with AsyncMarketplaceEntitlementServiceClient() as s3:
        # Example: call the get_entitlements operation
        response = await s3.get_entitlements()
        print(response["entitlements"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_entitlement_service import AsyncMarketplaceEntitlementServiceClient
from capo_marketplace_entitlement_service.error import InternalServiceErrorException


async def main():
    async with AsyncMarketplaceEntitlementServiceClient() as s3:
        try:
            await s3.get_entitlements()
        except InternalServiceErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_entitlement_service import AsyncMarketplaceEntitlementServiceClient


async def main():
    async with AsyncMarketplaceEntitlementServiceClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.get_entitlements()

        # Override per operation
        response = await s3.get_entitlements(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.get_entitlements(config_overrides={"retry_max_attempts": 1})
```
