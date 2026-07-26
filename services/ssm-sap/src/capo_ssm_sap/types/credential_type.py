"""Generated from Smithy shape ``com.amazonaws.ssmsap#CredentialType``."""

from typing import Literal, TypeAlias, cast

CredentialType: TypeAlias = Literal["ADMIN",]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialType) -> str:
    return value


def deserialize_json(data: str) -> CredentialType:
    return cast(CredentialType, data)
