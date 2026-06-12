"""Generated from Smithy shape ``com.amazonaws.workdocs#ContentCategoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "IMAGE",
        "DOCUMENT",
        "PDF",
        "SPREADSHEET",
        "PRESENTATION",
        "AUDIO",
        "VIDEO",
        "SOURCE_CODE",
        "OTHER",
    )
)


def serialize_json(value: ContentCategoryType) -> str:
    return value


def deserialize_json(data: str) -> ContentCategoryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentCategoryType value: {data!r}")
    return cast(ContentCategoryType, data)
