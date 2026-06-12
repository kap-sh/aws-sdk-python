"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ImportStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Deleting",
    )
)


def serialize_json(value: ImportStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportStatus value: {data!r}")
    return cast(ImportStatus, data)
