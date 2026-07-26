"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringType``."""

from typing import Literal, TypeAlias, cast

PeeringType: TypeAlias = Literal["TRANSIT_GATEWAY",]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringType) -> str:
    return value


def deserialize_json(data: str) -> PeeringType:
    return cast(PeeringType, data)
