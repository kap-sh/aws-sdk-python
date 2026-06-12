"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AliasAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AliasAttributeType: TypeAlias = Literal[
    "phone_number",
    "email",
    "preferred_username",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "phone_number",
        "email",
        "preferred_username",
    )
)


def serialize_aws_json_1_1(value: AliasAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AliasAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AliasAttributeType value: {data!r}")
    return cast(AliasAttributeType, data)
