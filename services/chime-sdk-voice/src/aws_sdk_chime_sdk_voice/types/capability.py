"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Capability``."""

from typing import Literal, TypeAlias, cast

Capability: TypeAlias = Literal[
    "Voice",
    "SMS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Capability) -> str:
    return value


def deserialize_json(data: str) -> Capability:
    return cast(Capability, data)
