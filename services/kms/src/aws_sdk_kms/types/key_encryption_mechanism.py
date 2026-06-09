"""Generated from Smithy shape ``com.amazonaws.kms#KeyEncryptionMechanism``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

KeyEncryptionMechanism: TypeAlias = Literal["RSAES_OAEP_SHA_256",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RSAES_OAEP_SHA_256",))


def serialize_aws_json_1_1(value: KeyEncryptionMechanism) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyEncryptionMechanism:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyEncryptionMechanism value: {data!r}")
    return cast(KeyEncryptionMechanism, data)
