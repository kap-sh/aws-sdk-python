"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

SearchResourceType: TypeAlias = Literal[
    "FOLDER",
    "DOCUMENT",
    "COMMENT",
    "DOCUMENT_VERSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLDER",
        "DOCUMENT",
        "COMMENT",
        "DOCUMENT_VERSION",
    )
)


def serialize_json(value: SearchResourceType) -> str:
    return value


def deserialize_json(data: str) -> SearchResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchResourceType value: {data!r}")
    return cast(SearchResourceType, data)
