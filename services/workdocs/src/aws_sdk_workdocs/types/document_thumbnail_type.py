"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentThumbnailType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

DocumentThumbnailType: TypeAlias = Literal[
    "SMALL",
    "SMALL_HQ",
    "LARGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMALL",
        "SMALL_HQ",
        "LARGE",
    )
)


def serialize_json(value: DocumentThumbnailType) -> str:
    return value


def deserialize_json(data: str) -> DocumentThumbnailType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentThumbnailType value: {data!r}")
    return cast(DocumentThumbnailType, data)
