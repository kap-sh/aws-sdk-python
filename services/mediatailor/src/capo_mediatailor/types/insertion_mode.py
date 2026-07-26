"""Generated from Smithy shape ``com.amazonaws.mediatailor#InsertionMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Insertion Mode controls whether players can use stitched or guided ad insertion.</p>"""
InsertionMode: TypeAlias = Literal[
    "STITCHED_ONLY",
    "PLAYER_SELECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsertionMode) -> str:
    return value


def deserialize_json(data: str) -> InsertionMode:
    return cast(InsertionMode, data)
