"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AllowMessages``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

AllowMessages: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NONE",
    )
)


def serialize_json(value: AllowMessages) -> str:
    return value


def deserialize_json(data: str) -> AllowMessages:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowMessages value: {data!r}")
    return cast(AllowMessages, data)
