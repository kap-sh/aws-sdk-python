"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RiskDecisionType``."""

from typing import Literal, TypeAlias, cast

RiskDecisionType: TypeAlias = Literal[
    "NoRisk",
    "AccountTakeover",
    "Block",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RiskDecisionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RiskDecisionType:
    return cast(RiskDecisionType, data)
