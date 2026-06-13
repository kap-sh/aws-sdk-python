"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DurationUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

DurationUnits: TypeAlias = Literal["MONTHS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MONTHS",))


def serialize_json(value: DurationUnits) -> str:
    return value


def deserialize_json(data: str) -> DurationUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DurationUnits value: {data!r}")
    return cast(DurationUnits, data)
