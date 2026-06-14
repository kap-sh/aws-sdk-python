"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

SuppressionUnit: TypeAlias = Literal[
    "SECONDS",
    "MINUTES",
    "HOURS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECONDS",
        "MINUTES",
        "HOURS",
    )
)


def serialize_aws_json_1_1(value: SuppressionUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuppressionUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SuppressionUnit value: {data!r}")
    return cast(SuppressionUnit, data)
