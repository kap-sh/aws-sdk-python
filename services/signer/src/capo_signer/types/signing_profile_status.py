"""Generated from Smithy shape ``com.amazonaws.signer#SigningProfileStatus``."""

from typing import Literal, TypeAlias, cast

SigningProfileStatus: TypeAlias = Literal[
    "Active",
    "Canceled",
    "Revoked",
]


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> SigningProfileStatus:
    return cast(SigningProfileStatus, data)
