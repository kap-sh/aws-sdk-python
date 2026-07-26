"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationRuleMode``."""

from typing import Literal, TypeAlias, cast

OrganizationRuleMode: TypeAlias = Literal[
    "AnyAllowed",
    "NoneAllowed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrganizationRuleMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OrganizationRuleMode:
    return cast(OrganizationRuleMode, data)
