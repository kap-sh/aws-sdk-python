"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseButton``."""

from typing import Literal, TypeAlias, cast

"""<p>The mouse button to use for a browser mouse action.</p>"""
MouseButton: TypeAlias = Literal[
    "LEFT",
    "RIGHT",
    "MIDDLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MouseButton) -> str:
    return value


def deserialize_json(data: str) -> MouseButton:
    return cast(MouseButton, data)
