"""Generated from Smithy shape ``com.amazonaws.connect#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EncryptionType: TypeAlias = Literal["KMS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS",))


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
