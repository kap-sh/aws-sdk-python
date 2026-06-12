"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdvancedSecurityModeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AdvancedSecurityModeType: TypeAlias = Literal[
    "OFF",
    "AUDIT",
    "ENFORCED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "AUDIT",
        "ENFORCED",
    )
)


def serialize_aws_json_1_1(value: AdvancedSecurityModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdvancedSecurityModeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdvancedSecurityModeType value: {data!r}")
    return cast(AdvancedSecurityModeType, data)
