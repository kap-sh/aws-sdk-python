"""Generated from Smithy shape ``com.amazonaws.groundstation#EirpUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

EirpUnits: TypeAlias = Literal["dBW",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("dBW",))


def serialize_json(value: EirpUnits) -> str:
    return value


def deserialize_json(data: str) -> EirpUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EirpUnits value: {data!r}")
    return cast(EirpUnits, data)
