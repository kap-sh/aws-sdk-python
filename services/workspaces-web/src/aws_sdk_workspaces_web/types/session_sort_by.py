"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

SessionSortBy: TypeAlias = Literal[
    "StartTimeAscending",
    "StartTimeDescending",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StartTimeAscending",
        "StartTimeDescending",
    )
)


def serialize_json(value: SessionSortBy) -> str:
    return value


def deserialize_json(data: str) -> SessionSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionSortBy value: {data!r}")
    return cast(SessionSortBy, data)
