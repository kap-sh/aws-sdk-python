"""Generated from Smithy shape ``com.amazonaws.workdocs#ResponseItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

ResponseItemType: TypeAlias = Literal[
    "DOCUMENT",
    "FOLDER",
    "COMMENT",
    "DOCUMENT_VERSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT",
        "FOLDER",
        "COMMENT",
        "DOCUMENT_VERSION",
    )
)


def serialize_json(value: ResponseItemType) -> str:
    return value


def deserialize_json(data: str) -> ResponseItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseItemType value: {data!r}")
    return cast(ResponseItemType, data)
