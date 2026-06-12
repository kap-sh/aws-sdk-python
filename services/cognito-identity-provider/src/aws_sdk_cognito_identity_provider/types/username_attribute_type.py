"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UsernameAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UsernameAttributeType: TypeAlias = Literal[
    "phone_number",
    "email",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "phone_number",
        "email",
    )
)


def serialize_aws_json_1_1(value: UsernameAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsernameAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsernameAttributeType value: {data!r}")
    return cast(UsernameAttributeType, data)
