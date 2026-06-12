"""Generated from Smithy shape ``com.amazonaws.ssoadmin#KmsKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

KmsKeyType: TypeAlias = Literal[
    "AWS_OWNED_KMS_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KMS_KEY",
        "CUSTOMER_MANAGED_KEY",
    )
)


def serialize_aws_json_1_1(value: KmsKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KmsKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KmsKeyType value: {data!r}")
    return cast(KmsKeyType, data)
