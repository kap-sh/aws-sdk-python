"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkState``."""

from typing import Literal, TypeAlias, cast

LinkState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkState) -> str:
    return value


def deserialize_json(data: str) -> LinkState:
    return cast(LinkState, data)
