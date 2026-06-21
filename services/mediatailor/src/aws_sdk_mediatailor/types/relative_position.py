"""Generated from Smithy shape ``com.amazonaws.mediatailor#RelativePosition``."""

from typing import Literal, TypeAlias, cast

RelativePosition: TypeAlias = Literal[
    "BEFORE_PROGRAM",
    "AFTER_PROGRAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: RelativePosition) -> str:
    return value


def deserialize_json(data: str) -> RelativePosition:
    return cast(RelativePosition, data)
