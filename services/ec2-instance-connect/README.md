# Getting Started

## Installation

```
pip install aws-sdk-ec2-instance-connect
```

## Usage

```python
from aws_sdk_ec2_instance_connect import AsyncEC2InstanceConnectClient


async def main():
    async with AsyncEC2InstanceConnectClient() as s3:
        # Example: call the send_serial_console_ssh_public_key operation
        response = await s3.send_serial_console_ssh_public_key()
        print(response["request_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_ec2_instance_connect import AsyncEC2InstanceConnectClient
from aws_sdk_ec2_instance_connect.error import AuthException


async def main():
    async with AsyncEC2InstanceConnectClient() as s3:
        try:
            await s3.send_serial_console_ssh_public_key()
        except AuthException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_ec2_instance_connect import AsyncEC2InstanceConnectClient


async def main():
    async with AsyncEC2InstanceConnectClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.send_serial_console_ssh_public_key()

        # Override per operation
        response = await s3.send_serial_console_ssh_public_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.send_serial_console_ssh_public_key(config_overrides={"retry_max_attempts": 1})
```
