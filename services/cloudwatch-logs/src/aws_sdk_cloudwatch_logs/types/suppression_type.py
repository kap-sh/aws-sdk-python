"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

SuppressionType: TypeAlias = Literal[
    "LIMITED",
    "INFINITE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIMITED",
        "INFINITE",
    )
)


def serialize_aws_json_1_1(value: SuppressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuppressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SuppressionType value: {data!r}")
    return cast(SuppressionType, data)
