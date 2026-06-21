"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ColorTheme``."""

from typing import Literal, TypeAlias, cast

ColorTheme: TypeAlias = Literal[
    "Light",
    "Dark",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColorTheme) -> str:
    return value


def deserialize_json(data: str) -> ColorTheme:
    return cast(ColorTheme, data)
