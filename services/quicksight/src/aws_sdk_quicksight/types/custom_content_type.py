"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomContentType``."""

from typing import Literal, TypeAlias, cast

CustomContentType: TypeAlias = Literal[
    "IMAGE",
    "OTHER_EMBEDDED_CONTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomContentType) -> str:
    return value


def deserialize_json(data: str) -> CustomContentType:
    return cast(CustomContentType, data)
