"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

InferredWorkloadType: TypeAlias = Literal[
    "AmazonEmr",
    "ApacheCassandra",
    "ApacheHadoop",
    "Memcached",
    "Nginx",
    "PostgreSql",
    "Redis",
    "Kafka",
    "SQLServer",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AmazonEmr",
        "ApacheCassandra",
        "ApacheHadoop",
        "Memcached",
        "Nginx",
        "PostgreSql",
        "Redis",
        "Kafka",
        "SQLServer",
    )
)


def serialize_aws_json_1_0(value: InferredWorkloadType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferredWorkloadType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferredWorkloadType value: {data!r}")
    return cast(InferredWorkloadType, data)
