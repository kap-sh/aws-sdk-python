"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeletionProtectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

DeletionProtectionType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: DeletionProtectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletionProtectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletionProtectionType value: {data!r}")
    return cast(DeletionProtectionType, data)
