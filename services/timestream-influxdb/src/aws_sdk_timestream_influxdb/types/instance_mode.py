"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InstanceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

InstanceMode: TypeAlias = Literal[
    "PRIMARY",
    "STANDBY",
    "REPLICA",
    "INGEST",
    "QUERY",
    "COMPACT",
    "PROCESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "STANDBY",
        "REPLICA",
        "INGEST",
        "QUERY",
        "COMPACT",
        "PROCESS",
    )
)


def serialize_aws_json_1_0(value: InstanceMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceMode value: {data!r}")
    return cast(InstanceMode, data)
