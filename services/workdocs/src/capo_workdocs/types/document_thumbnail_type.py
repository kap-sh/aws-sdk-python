"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentThumbnailType``."""

from typing import Literal, TypeAlias, cast

DocumentThumbnailType: TypeAlias = Literal[
    "SMALL",
    "SMALL_HQ",
    "LARGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentThumbnailType) -> str:
    return value


def deserialize_json(data: str) -> DocumentThumbnailType:
    return cast(DocumentThumbnailType, data)
