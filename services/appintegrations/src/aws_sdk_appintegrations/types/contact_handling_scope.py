"""Generated from Smithy shape ``com.amazonaws.appintegrations#ContactHandlingScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appintegrations.errors import DeserializationError

ContactHandlingScope: TypeAlias = Literal[
    "CROSS_CONTACTS",
    "PER_CONTACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CROSS_CONTACTS",
        "PER_CONTACT",
    )
)


def serialize_json(value: ContactHandlingScope) -> str:
    return value


def deserialize_json(data: str) -> ContactHandlingScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactHandlingScope value: {data!r}")
    return cast(ContactHandlingScope, data)
