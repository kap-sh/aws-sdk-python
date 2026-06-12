"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RecoveryOptionNameType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

RecoveryOptionNameType: TypeAlias = Literal[
    "verified_email",
    "verified_phone_number",
    "admin_only",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "verified_email",
        "verified_phone_number",
        "admin_only",
    )
)


def serialize_aws_json_1_1(value: RecoveryOptionNameType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecoveryOptionNameType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecoveryOptionNameType value: {data!r}")
    return cast(RecoveryOptionNameType, data)
