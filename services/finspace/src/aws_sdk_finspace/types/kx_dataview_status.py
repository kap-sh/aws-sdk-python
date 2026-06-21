"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewStatus``."""

from typing import Literal, TypeAlias, cast

KxDataviewStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewStatus) -> str:
    return value


def deserialize_json(data: str) -> KxDataviewStatus:
    return cast(KxDataviewStatus, data)
