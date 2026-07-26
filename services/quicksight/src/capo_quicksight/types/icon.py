"""Generated from Smithy shape ``com.amazonaws.quicksight#Icon``."""

from typing import Literal, TypeAlias, cast

Icon: TypeAlias = Literal[
    "CARET_UP",
    "CARET_DOWN",
    "PLUS",
    "MINUS",
    "ARROW_UP",
    "ARROW_DOWN",
    "ARROW_LEFT",
    "ARROW_UP_LEFT",
    "ARROW_DOWN_LEFT",
    "ARROW_RIGHT",
    "ARROW_UP_RIGHT",
    "ARROW_DOWN_RIGHT",
    "FACE_UP",
    "FACE_DOWN",
    "FACE_FLAT",
    "ONE_BAR",
    "TWO_BAR",
    "THREE_BAR",
    "CIRCLE",
    "TRIANGLE",
    "SQUARE",
    "FLAG",
    "THUMBS_UP",
    "THUMBS_DOWN",
    "CHECKMARK",
    "X",
]


# --- restJson1 ser/de ---
def serialize_json(value: Icon) -> str:
    return value


def deserialize_json(data: str) -> Icon:
    return cast(Icon, data)
