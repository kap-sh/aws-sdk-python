
# aws-sdk-python

Modern AWS SDK for Python — async-native, fully typed, and generated from official Smithy models.

## Installation

```bash
pip install aws-sdk-s3
```

Each service is distributed as its own package (e.g. `aws-sdk-s3`, `aws-sdk-ec2`).

## Features

- **async and sync** — Use the same API for both async and sync code, with support for asyncio and [trio](https://trio.readthedocs.io).
- **WASM support** — Runs in WASM environments via [Pyodide](https://pyodide.org).
- **typed and documented** — Fully typed and documented for a better developer experience.
- **simple inputs** — No need to import separate parameter classes; nested inputs are fully typed via [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict).
- **generated from Smithy models** — The SDK is generated from the official [Smithy](https://smithy.io) models describing AWS APIs, ensuring accuracy and consistency.
- **zero runtime overhead** — Codegen produces dedicated serialization and deserialization code for each operation, avoiding reflection.
- **interchangeable input/output** — Input and output types use the same [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), so you can pass a response directly as input when appropriate.
- **built on [zapros](https://zapros.dev)** — A modern HTTP client for Python that abstracts HTTP semantics from the transport implementation.

## Usage

```python
from aws_sdk_s3 import S3Client

with S3Client() as s3:
    response = s3.create_bucket("capo")
    print(response)
```

Async:

```python
from aws_sdk_s3 import AsyncS3Client

async def main():
    async with AsyncS3Client() as s3:
        response = await s3.create_bucket("capo")
        print(response)
```

See the README for each service under the [`services/`](services/) directory for detailed usage including pagination, waiters, and error handling.

## Services

| Service | Package |
|---------|---------|
| DynamoDB | `aws-sdk-dynamodb` |
| EC2 | `aws-sdk-ec2` |
| ECS | `aws-sdk-ecs` |
| EKS | `aws-sdk-eks` |
| KMS | `aws-sdk-kms` |
| Lambda | `aws-sdk-lambda` |
| S3 | `aws-sdk-s3` |
| Secrets Manager | `aws-sdk-secrets-manager` |

More services coming soon.
