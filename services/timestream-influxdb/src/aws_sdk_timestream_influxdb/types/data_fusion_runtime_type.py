"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DataFusionRuntimeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

DataFusionRuntimeType: TypeAlias = Literal[
    "multi-thread",
    "multi-thread-alt",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "multi-thread",
        "multi-thread-alt",
    )
)


def serialize_aws_json_1_0(value: DataFusionRuntimeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataFusionRuntimeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataFusionRuntimeType value: {data!r}")
    return cast(DataFusionRuntimeType, data)
