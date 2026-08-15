"""Generated from Smithy shape ``com.amazonaws.lambda#PropagateTagsMode``."""

from typing import Literal, TypeAlias, cast

PropagateTagsMode: TypeAlias = Literal[
    "None",
    "Explicit",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropagateTagsMode) -> str:
    return value


def deserialize_json(data: str) -> PropagateTagsMode:
    return cast(PropagateTagsMode, data)
