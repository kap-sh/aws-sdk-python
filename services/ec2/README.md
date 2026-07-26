# Getting Started

## Installation

```
pip install capo-ec2
```

## Usage

```python
from capo_ec2 import AsyncEC2Client


async def main():
    async with AsyncEC2Client() as s3:
        # Example: call the accept_address_transfer operation
        response = await s3.accept_address_transfer()
        print(response["address_transfer"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ec2 import AsyncEC2Client


async def main():
    async with AsyncEC2Client() as s3:
        # Example: paginate over describe_addresses_attribute
        async for item in s3.iter_describe_addresses_attribute():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_ec2 import AsyncEC2Client


async def main():
    async with AsyncEC2Client() as s3:
        # Example: wait for vpc_peering_connection_exists
        await s3.wait_until_vpc_peering_connection_exists(max_wait_time=300)
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ec2 import AsyncEC2Client


async def main():
    async with AsyncEC2Client() as s3:
        # Default: 3 attempts for every operation
        response = await s3.accept_address_transfer()

        # Override per operation
        response = await s3.accept_address_transfer(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.accept_address_transfer(config_overrides={"retry_max_attempts": 1})
```
