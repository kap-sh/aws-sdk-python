# Getting Started

## Installation

```
pip install capo-direct-connect
```

## Usage

```python
from capo_direct_connect import AsyncDirectConnectClient


async def main():
    async with AsyncDirectConnectClient() as s3:
        # Example: call the accept_direct_connect_gateway_association_proposal operation
        response = await s3.accept_direct_connect_gateway_association_proposal()
        print(response["direct_connect_gateway_association"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_direct_connect import AsyncDirectConnectClient
from capo_direct_connect.error import DirectConnectClientException


async def main():
    async with AsyncDirectConnectClient() as s3:
        try:
            await s3.accept_direct_connect_gateway_association_proposal()
        except DirectConnectClientException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_direct_connect import AsyncDirectConnectClient


async def main():
    async with AsyncDirectConnectClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.accept_direct_connect_gateway_association_proposal()

        # Override per operation
        response = await s3.accept_direct_connect_gateway_association_proposal(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.accept_direct_connect_gateway_association_proposal(config_overrides={"retry_max_attempts": 1})
```
