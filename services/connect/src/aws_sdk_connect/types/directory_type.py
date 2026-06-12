"""Generated from Smithy shape ``com.amazonaws.connect#DirectoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DirectoryType: TypeAlias = Literal[
    "SAML",
    "CONNECT_MANAGED",
    "EXISTING_DIRECTORY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAML",
        "CONNECT_MANAGED",
        "EXISTING_DIRECTORY",
    )
)


def serialize_json(value: DirectoryType) -> str:
    return value


def deserialize_json(data: str) -> DirectoryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectoryType value: {data!r}")
    return cast(DirectoryType, data)
