"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

DurationType: TypeAlias = Literal[
    "hours",
    "minutes",
    "seconds",
    "milliseconds",
    "days",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "hours",
        "minutes",
        "seconds",
        "milliseconds",
        "days",
    )
)


def serialize_aws_json_1_0(value: DurationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DurationType value: {data!r}")
    return cast(DurationType, data)
