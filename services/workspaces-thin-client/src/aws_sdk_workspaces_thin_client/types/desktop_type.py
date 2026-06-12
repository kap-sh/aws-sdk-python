"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DesktopType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

DesktopType: TypeAlias = Literal[
    "workspaces",
    "appstream",
    "workspaces-web",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "workspaces",
        "appstream",
        "workspaces-web",
    )
)


def serialize_json(value: DesktopType) -> str:
    return value


def deserialize_json(data: str) -> DesktopType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DesktopType value: {data!r}")
    return cast(DesktopType, data)
