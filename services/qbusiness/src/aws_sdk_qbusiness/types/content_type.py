"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentType``."""

from typing import Literal, TypeAlias, cast

ContentType: TypeAlias = Literal[
    "PDF",
    "HTML",
    "MS_WORD",
    "PLAIN_TEXT",
    "PPT",
    "RTF",
    "XML",
    "XSLT",
    "MS_EXCEL",
    "CSV",
    "JSON",
    "MD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    return cast(ContentType, data)
