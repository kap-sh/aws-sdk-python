"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ShareStatus``."""

from typing import Literal, TypeAlias, cast

ShareStatus: TypeAlias = Literal[
    "NOT_SHARED",
    "INITIATED",
    "SHARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareStatus:
    return cast(ShareStatus, data)
