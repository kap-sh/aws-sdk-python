"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

SuppressionState: TypeAlias = Literal[
    "SUPPRESSED",
    "UNSUPPRESSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUPPRESSED",
        "UNSUPPRESSED",
    )
)


def serialize_aws_json_1_1(value: SuppressionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuppressionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SuppressionState value: {data!r}")
    return cast(SuppressionState, data)
