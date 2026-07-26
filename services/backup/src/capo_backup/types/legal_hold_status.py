"""Generated from Smithy shape ``com.amazonaws.backup#LegalHoldStatus``."""

from typing import Literal, TypeAlias, cast

LegalHoldStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CANCELING",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LegalHoldStatus) -> str:
    return value


def deserialize_json(data: str) -> LegalHoldStatus:
    return cast(LegalHoldStatus, data)
