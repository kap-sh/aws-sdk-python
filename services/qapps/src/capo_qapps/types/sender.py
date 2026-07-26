"""Generated from Smithy shape ``com.amazonaws.qapps#Sender``."""

from typing import Literal, TypeAlias, cast

Sender: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: Sender) -> str:
    return value


def deserialize_json(data: str) -> Sender:
    return cast(Sender, data)
