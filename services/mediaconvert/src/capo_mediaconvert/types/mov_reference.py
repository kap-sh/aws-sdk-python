"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovReference``."""

from typing import Literal, TypeAlias, cast

"""Always keep the default value (SELF_CONTAINED) for this setting."""
MovReference: TypeAlias = Literal[
    "SELF_CONTAINED",
    "EXTERNAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MovReference) -> str:
    return value


def deserialize_json(data: str) -> MovReference:
    return cast(MovReference, data)
