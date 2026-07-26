"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DesktopType``."""

from typing import Literal, TypeAlias, cast

DesktopType: TypeAlias = Literal[
    "workspaces",
    "appstream",
    "workspaces-web",
]


# --- restJson1 ser/de ---
def serialize_json(value: DesktopType) -> str:
    return value


def deserialize_json(data: str) -> DesktopType:
    return cast(DesktopType, data)
