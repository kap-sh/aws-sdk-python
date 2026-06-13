"""Generated from Smithy shape ``com.amazonaws.quicksight#CapabilityState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CapabilityState: TypeAlias = Literal["DENY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DENY",))


def serialize_json(value: CapabilityState) -> str:
    return value


def deserialize_json(data: str) -> CapabilityState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityState value: {data!r}")
    return cast(CapabilityState, data)
