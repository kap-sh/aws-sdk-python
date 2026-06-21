"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormButtonsPosition``."""

from typing import Literal, TypeAlias, cast

FormButtonsPosition: TypeAlias = Literal[
    "top",
    "bottom",
    "top_and_bottom",
]


# --- restJson1 ser/de ---
def serialize_json(value: FormButtonsPosition) -> str:
    return value


def deserialize_json(data: str) -> FormButtonsPosition:
    return cast(FormButtonsPosition, data)
