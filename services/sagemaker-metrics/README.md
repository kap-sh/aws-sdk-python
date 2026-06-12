# Getting Started

## Installation

```
pip install aws-sdk-sagemaker-metrics
```

## Usage

```python
from aws_sdk_sagemaker_metrics import AsyncSageMakerMetricsClient


async def main():
    async with AsyncSageMakerMetricsClient() as s3:
        # Example: call the batch_get_metrics operation
        response = await s3.batch_get_metrics()
        print(response["metric_query_results"])
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_sagemaker_metrics import AsyncSageMakerMetricsClient


async def main():
    async with AsyncSageMakerMetricsClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.batch_get_metrics()

        # Override per operation
        response = await s3.batch_get_metrics(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.batch_get_metrics(config_overrides={"retry_max_attempts": 1})
```
