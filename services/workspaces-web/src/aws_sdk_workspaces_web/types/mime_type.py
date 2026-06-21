"""Generated from Smithy shape ``com.amazonaws.workspacesweb#MimeType``."""

from typing import Literal, TypeAlias, cast

MimeType: TypeAlias = Literal[
    "image/png",
    "image/jpeg",
    "image/x-icon",
]


# --- restJson1 ser/de ---
def serialize_json(value: MimeType) -> str:
    return value


def deserialize_json(data: str) -> MimeType:
    return cast(MimeType, data)
