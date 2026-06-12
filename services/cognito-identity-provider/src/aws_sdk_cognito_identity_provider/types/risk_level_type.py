"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RiskLevelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

RiskLevelType: TypeAlias = Literal[
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Low",
        "Medium",
        "High",
    )
)


def serialize_aws_json_1_1(value: RiskLevelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RiskLevelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RiskLevelType value: {data!r}")
    return cast(RiskLevelType, data)
