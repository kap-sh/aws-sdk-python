"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "json",
    "plain",
    "w3c",
    "raw",
    "parquet",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "plain",
        "w3c",
        "raw",
        "parquet",
    )
)


def serialize_aws_json_1_1(value: OutputFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
