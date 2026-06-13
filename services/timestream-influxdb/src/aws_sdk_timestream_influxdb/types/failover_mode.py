"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#FailoverMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

FailoverMode: TypeAlias = Literal[
    "AUTOMATIC",
    "NO_FAILOVER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "NO_FAILOVER",
    )
)


def serialize_aws_json_1_0(value: FailoverMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FailoverMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailoverMode value: {data!r}")
    return cast(FailoverMode, data)
