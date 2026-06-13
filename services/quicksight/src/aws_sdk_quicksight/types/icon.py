"""Generated from Smithy shape ``com.amazonaws.quicksight#Icon``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: Icon) -> str:
    return value


def deserialize_json(data: str) -> Icon:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Icon value: {data!r}")
    return cast(Icon, data)
