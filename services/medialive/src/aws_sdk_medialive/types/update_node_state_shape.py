"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateNodeStateShape``."""

from typing import Literal, TypeAlias, cast

"""Used in UpdateNodeStateRequest."""
UpdateNodeStateShape: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodeStateShape) -> str:
    return value


def deserialize_json(data: str) -> UpdateNodeStateShape:
    return cast(UpdateNodeStateShape, data)
