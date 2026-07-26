"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRulePhaseAction``."""

from typing import Literal, TypeAlias, cast

ProxyRulePhaseAction: TypeAlias = Literal[
    "ALLOW",
    "DENY",
    "ALERT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRulePhaseAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProxyRulePhaseAction:
    return cast(ProxyRulePhaseAction, data)
