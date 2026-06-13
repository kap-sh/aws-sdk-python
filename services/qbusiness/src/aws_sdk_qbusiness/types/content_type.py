"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
