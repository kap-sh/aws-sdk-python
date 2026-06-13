"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#EngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

EngineType: TypeAlias = Literal[
    "INFLUXDB_V2",
    "INFLUXDB_V3_CORE",
    "INFLUXDB_V3_ENTERPRISE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFLUXDB_V2",
        "INFLUXDB_V3_CORE",
        "INFLUXDB_V3_ENTERPRISE",
    )
)


def serialize_aws_json_1_0(value: EngineType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngineType value: {data!r}")
    return cast(EngineType, data)
