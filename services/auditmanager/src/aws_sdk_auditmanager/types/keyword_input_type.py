"""Generated from Smithy shape ``com.amazonaws.auditmanager#KeywordInputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

KeywordInputType: TypeAlias = Literal[
    "SELECT_FROM_LIST",
    "UPLOAD_FILE",
    "INPUT_TEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELECT_FROM_LIST",
        "UPLOAD_FILE",
        "INPUT_TEXT",
    )
)


def serialize_json(value: KeywordInputType) -> str:
    return value


def deserialize_json(data: str) -> KeywordInputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeywordInputType value: {data!r}")
    return cast(KeywordInputType, data)
