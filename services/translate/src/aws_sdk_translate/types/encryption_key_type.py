"""Generated from Smithy shape ``com.amazonaws.translate#EncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

EncryptionKeyType: TypeAlias = Literal["KMS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS",))


def serialize_aws_json_1_1(value: EncryptionKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionKeyType value: {data!r}")
    return cast(EncryptionKeyType, data)
