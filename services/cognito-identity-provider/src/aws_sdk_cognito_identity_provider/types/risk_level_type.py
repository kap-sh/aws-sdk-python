"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RiskLevelType``."""

from typing import Literal, TypeAlias, cast

RiskLevelType: TypeAlias = Literal[
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RiskLevelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RiskLevelType:
    return cast(RiskLevelType, data)
