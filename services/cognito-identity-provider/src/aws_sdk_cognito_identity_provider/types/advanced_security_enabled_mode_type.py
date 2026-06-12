"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdvancedSecurityEnabledModeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AdvancedSecurityEnabledModeType: TypeAlias = Literal[
    "AUDIT",
    "ENFORCED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIT",
        "ENFORCED",
    )
)


def serialize_aws_json_1_1(value: AdvancedSecurityEnabledModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdvancedSecurityEnabledModeType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdvancedSecurityEnabledModeType value: {data!r}"
        )
    return cast(AdvancedSecurityEnabledModeType, data)
