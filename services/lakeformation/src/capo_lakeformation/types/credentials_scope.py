"""Generated from Smithy shape ``com.amazonaws.lakeformation#CredentialsScope``."""

from typing import Literal, TypeAlias, cast

CredentialsScope: TypeAlias = Literal[
    "READ",
    "READWRITE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsScope) -> str:
    return value


def deserialize_json(data: str) -> CredentialsScope:
    return cast(CredentialsScope, data)
