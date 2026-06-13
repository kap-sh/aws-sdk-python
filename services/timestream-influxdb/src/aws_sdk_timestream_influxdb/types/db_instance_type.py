"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbInstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

DbInstanceType: TypeAlias = Literal[
    "db.influx.medium",
    "db.influx.large",
    "db.influx.xlarge",
    "db.influx.2xlarge",
    "db.influx.4xlarge",
    "db.influx.8xlarge",
    "db.influx.12xlarge",
    "db.influx.16xlarge",
    "db.influx.24xlarge",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "db.influx.medium",
        "db.influx.large",
        "db.influx.xlarge",
        "db.influx.2xlarge",
        "db.influx.4xlarge",
        "db.influx.8xlarge",
        "db.influx.12xlarge",
        "db.influx.16xlarge",
        "db.influx.24xlarge",
    )
)


def serialize_aws_json_1_0(value: DbInstanceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbInstanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DbInstanceType value: {data!r}")
    return cast(DbInstanceType, data)
