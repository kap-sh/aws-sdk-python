"""Generated from Smithy shape ``com.amazonaws.qapps#CardType``."""

from typing import Literal, TypeAlias, cast

CardType: TypeAlias = Literal[
    "text-input",
    "q-query",
    "file-upload",
    "q-plugin",
    "form-input",
]


# --- restJson1 ser/de ---
def serialize_json(value: CardType) -> str:
    return value


def deserialize_json(data: str) -> CardType:
    return cast(CardType, data)
