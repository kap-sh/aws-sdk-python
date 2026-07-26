"""Generated from Smithy shape ``com.amazonaws.signer#SigningStatus``."""

from typing import Literal, TypeAlias, cast

SigningStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Succeeded",
]


# --- restJson1 ser/de ---
def serialize_json(value: SigningStatus) -> str:
    return value


def deserialize_json(data: str) -> SigningStatus:
    return cast(SigningStatus, data)
