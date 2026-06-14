"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "Active",
    "Terminated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Terminated",
    )
)


def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
