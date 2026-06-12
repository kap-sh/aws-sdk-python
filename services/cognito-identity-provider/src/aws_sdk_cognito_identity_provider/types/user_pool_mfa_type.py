"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolMfaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UserPoolMfaType: TypeAlias = Literal[
    "OFF",
    "ON",
    "OPTIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "ON",
        "OPTIONAL",
    )
)


def serialize_aws_json_1_1(value: UserPoolMfaType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserPoolMfaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserPoolMfaType value: {data!r}")
    return cast(UserPoolMfaType, data)
