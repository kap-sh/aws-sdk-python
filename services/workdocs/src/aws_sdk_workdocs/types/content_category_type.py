"""Generated from Smithy shape ``com.amazonaws.workdocs#ContentCategoryType``."""

from typing import Literal, TypeAlias, cast

ContentCategoryType: TypeAlias = Literal[
    "IMAGE",
    "DOCUMENT",
    "PDF",
    "SPREADSHEET",
    "PRESENTATION",
    "AUDIO",
    "VIDEO",
    "SOURCE_CODE",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentCategoryType) -> str:
    return value


def deserialize_json(data: str) -> ContentCategoryType:
    return cast(ContentCategoryType, data)
