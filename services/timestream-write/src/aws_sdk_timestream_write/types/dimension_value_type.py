"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DimensionValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

DimensionValueType: TypeAlias = Literal["VARCHAR",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("VARCHAR",))


def serialize_aws_json_1_0(value: DimensionValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DimensionValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionValueType value: {data!r}")
    return cast(DimensionValueType, data)
