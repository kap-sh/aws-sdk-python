"""Generated from Smithy shape ``com.amazonaws.batch#EFSTransitEncryption``."""

from typing import Literal, TypeAlias, cast

EFSTransitEncryption: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EFSTransitEncryption) -> str:
    return value


def deserialize_json(data: str) -> EFSTransitEncryption:
    return cast(EFSTransitEncryption, data)
