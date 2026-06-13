"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#LogFormats``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

LogFormats: TypeAlias = Literal["full",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("full",))


def serialize_aws_json_1_0(value: LogFormats) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogFormats:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogFormats value: {data!r}")
    return cast(LogFormats, data)
