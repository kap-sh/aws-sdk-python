"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

DocumentStatusType: TypeAlias = Literal[
    "INITIALIZED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "ACTIVE",
    )
)


def serialize_json(value: DocumentStatusType) -> str:
    return value


def deserialize_json(data: str) -> DocumentStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentStatusType value: {data!r}")
    return cast(DocumentStatusType, data)
