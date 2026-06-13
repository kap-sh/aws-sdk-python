"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PriceUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

PriceUnits: TypeAlias = Literal["HOURLY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HOURLY",))


def serialize_json(value: PriceUnits) -> str:
    return value


def deserialize_json(data: str) -> PriceUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PriceUnits value: {data!r}")
    return cast(PriceUnits, data)
