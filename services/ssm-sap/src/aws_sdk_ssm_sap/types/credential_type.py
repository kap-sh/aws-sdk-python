"""Generated from Smithy shape ``com.amazonaws.ssmsap#CredentialType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

CredentialType: TypeAlias = Literal["ADMIN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ADMIN",))


def serialize_json(value: CredentialType) -> str:
    return value


def deserialize_json(data: str) -> CredentialType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CredentialType value: {data!r}")
    return cast(CredentialType, data)
