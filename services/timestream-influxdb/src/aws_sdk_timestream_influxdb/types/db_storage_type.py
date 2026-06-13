"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

DbStorageType: TypeAlias = Literal[
    "InfluxIOIncludedT1",
    "InfluxIOIncludedT2",
    "InfluxIOIncludedT3",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InfluxIOIncludedT1",
        "InfluxIOIncludedT2",
        "InfluxIOIncludedT3",
    )
)


def serialize_aws_json_1_0(value: DbStorageType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DbStorageType value: {data!r}")
    return cast(DbStorageType, data)
