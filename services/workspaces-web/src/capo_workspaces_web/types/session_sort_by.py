"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionSortBy``."""

from typing import Literal, TypeAlias, cast

SessionSortBy: TypeAlias = Literal[
    "StartTimeAscending",
    "StartTimeDescending",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSortBy) -> str:
    return value


def deserialize_json(data: str) -> SessionSortBy:
    return cast(SessionSortBy, data)
