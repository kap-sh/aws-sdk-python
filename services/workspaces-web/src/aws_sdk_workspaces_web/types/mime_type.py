"""Generated from Smithy shape ``com.amazonaws.workspacesweb#MimeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

MimeType: TypeAlias = Literal[
    "image/png",
    "image/jpeg",
    "image/x-icon",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "image/png",
        "image/jpeg",
        "image/x-icon",
    )
)


def serialize_json(value: MimeType) -> str:
    return value


def deserialize_json(data: str) -> MimeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MimeType value: {data!r}")
    return cast(MimeType, data)
