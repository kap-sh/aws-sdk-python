"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

EncryptionKeyType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KEY",
        "CUSTOMER_MANAGED_KEY",
    )
)


def serialize_aws_json_1_1(value: EncryptionKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionKeyType value: {data!r}")
    return cast(EncryptionKeyType, data)
