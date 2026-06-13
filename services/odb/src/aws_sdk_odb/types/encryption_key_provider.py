"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

EncryptionKeyProvider: TypeAlias = Literal[
    "ORACLE_MANAGED",
    "AWS_KMS",
    "OKV",
    "OCI",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORACLE_MANAGED",
        "AWS_KMS",
        "OKV",
        "OCI",
    )
)


def serialize_aws_json_1_0(value: EncryptionKeyProvider) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionKeyProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionKeyProvider value: {data!r}")
    return cast(EncryptionKeyProvider, data)
