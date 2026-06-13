"""Generated from Smithy shape ``com.amazonaws.groundstation#TelemetrySinkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

TelemetrySinkType: TypeAlias = Literal["KINESIS_DATA_STREAM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KINESIS_DATA_STREAM",))


def serialize_json(value: TelemetrySinkType) -> str:
    return value


def deserialize_json(data: str) -> TelemetrySinkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TelemetrySinkType value: {data!r}")
    return cast(TelemetrySinkType, data)
