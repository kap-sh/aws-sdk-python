"""Generated from Smithy shape ``com.amazonaws.iot#DimensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DimensionType: TypeAlias = Literal["TOPIC_FILTER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TOPIC_FILTER",))


def serialize_json(value: DimensionType) -> str:
    return value


def deserialize_json(data: str) -> DimensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionType value: {data!r}")
    return cast(DimensionType, data)
