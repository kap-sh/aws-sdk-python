"""Generated from Smithy shape ``com.amazonaws.lakeformation#CredentialsScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

CredentialsScope: TypeAlias = Literal[
    "READ",
    "READWRITE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "READWRITE",
    )
)


def serialize_json(value: CredentialsScope) -> str:
    return value


def deserialize_json(data: str) -> CredentialsScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CredentialsScope value: {data!r}")
    return cast(CredentialsScope, data)
