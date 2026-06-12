"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolTierType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UserPoolTierType: TypeAlias = Literal[
    "LITE",
    "ESSENTIALS",
    "PLUS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LITE",
        "ESSENTIALS",
        "PLUS",
    )
)


def serialize_aws_json_1_1(value: UserPoolTierType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserPoolTierType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserPoolTierType value: {data!r}")
    return cast(UserPoolTierType, data)
