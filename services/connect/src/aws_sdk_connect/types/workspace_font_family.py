"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceFontFamily``."""

from typing import Literal, TypeAlias, cast

WorkspaceFontFamily: TypeAlias = Literal[
    "Arial",
    "Courier New",
    "Georgia",
    "Times New Roman",
    "Trebuchet",
    "Verdana",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceFontFamily) -> str:
    return value


def deserialize_json(data: str) -> WorkspaceFontFamily:
    return cast(WorkspaceFontFamily, data)
