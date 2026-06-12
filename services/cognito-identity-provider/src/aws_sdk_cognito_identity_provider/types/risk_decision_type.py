"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RiskDecisionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

RiskDecisionType: TypeAlias = Literal[
    "NoRisk",
    "AccountTakeover",
    "Block",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoRisk",
        "AccountTakeover",
        "Block",
    )
)


def serialize_aws_json_1_1(value: RiskDecisionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RiskDecisionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RiskDecisionType value: {data!r}")
    return cast(RiskDecisionType, data)
