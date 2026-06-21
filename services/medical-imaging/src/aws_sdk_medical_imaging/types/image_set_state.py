"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetState``."""

from typing import Literal, TypeAlias, cast

ImageSetState: TypeAlias = Literal[
    "ACTIVE",
    "LOCKED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetState) -> str:
    return value


def deserialize_json(data: str) -> ImageSetState:
    return cast(ImageSetState, data)
