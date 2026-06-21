"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#NumberSelectionBehavior``."""

from typing import Literal, TypeAlias, cast

NumberSelectionBehavior: TypeAlias = Literal[
    "PreferSticky",
    "AvoidSticky",
]


# --- restJson1 ser/de ---
def serialize_json(value: NumberSelectionBehavior) -> str:
    return value


def deserialize_json(data: str) -> NumberSelectionBehavior:
    return cast(NumberSelectionBehavior, data)
