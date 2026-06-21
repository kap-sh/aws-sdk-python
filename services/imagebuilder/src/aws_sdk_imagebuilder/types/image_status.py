"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageStatus``."""

from typing import Literal, TypeAlias, cast

ImageStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "BUILDING",
    "TESTING",
    "DISTRIBUTING",
    "INTEGRATING",
    "AVAILABLE",
    "CANCELLED",
    "FAILED",
    "DEPRECATED",
    "DELETED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageStatus:
    return cast(ImageStatus, data)
