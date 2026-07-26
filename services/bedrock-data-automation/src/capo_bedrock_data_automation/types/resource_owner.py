"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

"""Resource Owner"""
ResourceOwner: TypeAlias = Literal[
    "SERVICE",
    "ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOwner) -> str:
    return value


def deserialize_json(data: str) -> ResourceOwner:
    return cast(ResourceOwner, data)
