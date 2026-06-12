"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

PeeringType: TypeAlias = Literal["TRANSIT_GATEWAY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TRANSIT_GATEWAY",))


def serialize_json(value: PeeringType) -> str:
    return value


def deserialize_json(data: str) -> PeeringType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeeringType value: {data!r}")
    return cast(PeeringType, data)
