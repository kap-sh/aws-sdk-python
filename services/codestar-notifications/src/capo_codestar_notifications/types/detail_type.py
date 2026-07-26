"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DetailType``."""

from typing import Literal, TypeAlias, cast

DetailType: TypeAlias = Literal[
    "BASIC",
    "FULL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailType) -> str:
    return value


def deserialize_json(data: str) -> DetailType:
    return cast(DetailType, data)
