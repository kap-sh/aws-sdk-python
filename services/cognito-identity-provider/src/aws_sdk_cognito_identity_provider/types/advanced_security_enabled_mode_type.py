"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdvancedSecurityEnabledModeType``."""

from typing import Literal, TypeAlias, cast

AdvancedSecurityEnabledModeType: TypeAlias = Literal[
    "AUDIT",
    "ENFORCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedSecurityEnabledModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdvancedSecurityEnabledModeType:
    return cast(AdvancedSecurityEnabledModeType, data)
