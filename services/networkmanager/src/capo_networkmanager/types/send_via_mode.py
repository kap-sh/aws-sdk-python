"""Generated from Smithy shape ``com.amazonaws.networkmanager#SendViaMode``."""

from typing import Literal, TypeAlias, cast

SendViaMode: TypeAlias = Literal[
    "dual-hop",
    "single-hop",
]


# --- restJson1 ser/de ---
def serialize_json(value: SendViaMode) -> str:
    return value


def deserialize_json(data: str) -> SendViaMode:
    return cast(SendViaMode, data)
