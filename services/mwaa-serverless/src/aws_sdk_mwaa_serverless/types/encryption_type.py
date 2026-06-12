"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mwaa_serverless.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "AWS_MANAGED_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_MANAGED_KEY",
        "CUSTOMER_MANAGED_KEY",
    )
)


def serialize_aws_json_1_0(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
