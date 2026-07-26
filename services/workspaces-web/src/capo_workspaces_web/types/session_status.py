"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "Active",
    "Terminated",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
