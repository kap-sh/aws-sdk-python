"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

DocumentSourceType: TypeAlias = Literal[
    "ORIGINAL",
    "WITH_COMMENTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORIGINAL",
        "WITH_COMMENTS",
    )
)


def serialize_json(value: DocumentSourceType) -> str:
    return value


def deserialize_json(data: str) -> DocumentSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentSourceType value: {data!r}")
    return cast(DocumentSourceType, data)
