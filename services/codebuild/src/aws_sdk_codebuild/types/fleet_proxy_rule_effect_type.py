"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleEffectType``."""

from typing import Literal, TypeAlias, cast

FleetProxyRuleEffectType: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRuleEffectType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetProxyRuleEffectType:
    return cast(FleetProxyRuleEffectType, data)
