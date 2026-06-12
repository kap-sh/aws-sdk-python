"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ColumnStatisticsState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: ColumnStatisticsState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColumnStatisticsState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnStatisticsState value: {data!r}")
    return cast(ColumnStatisticsState, data)
