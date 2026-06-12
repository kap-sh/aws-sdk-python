"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactListImportAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

ContactListImportAction: TypeAlias = Literal[
    "DELETE",
    "PUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE",
        "PUT",
    )
)


def serialize_json(value: ContactListImportAction) -> str:
    return value


def deserialize_json(data: str) -> ContactListImportAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactListImportAction value: {data!r}")
    return cast(ContactListImportAction, data)
