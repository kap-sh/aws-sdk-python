"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#TracingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

TracingType: TypeAlias = Literal[
    "log",
    "jaeger",
    "disabled",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "log",
        "jaeger",
        "disabled",
    )
)


def serialize_aws_json_1_0(value: TracingType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TracingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TracingType value: {data!r}")
    return cast(TracingType, data)
