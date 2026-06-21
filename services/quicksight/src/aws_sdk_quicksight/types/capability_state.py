"""Generated from Smithy shape ``com.amazonaws.quicksight#CapabilityState``."""

from typing import Literal, TypeAlias, cast

CapabilityState: TypeAlias = Literal["DENY",]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityState) -> str:
    return value


def deserialize_json(data: str) -> CapabilityState:
    return cast(CapabilityState, data)
