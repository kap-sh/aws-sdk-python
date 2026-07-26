"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdvancedSecurityModeType``."""

from typing import Literal, TypeAlias, cast

AdvancedSecurityModeType: TypeAlias = Literal[
    "OFF",
    "AUDIT",
    "ENFORCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedSecurityModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdvancedSecurityModeType:
    return cast(AdvancedSecurityModeType, data)
