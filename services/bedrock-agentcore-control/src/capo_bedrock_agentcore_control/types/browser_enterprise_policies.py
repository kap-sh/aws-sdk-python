"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserEnterprisePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_enterprise_policy

BrowserEnterprisePolicies: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.browser_enterprise_policy.BrowserEnterprisePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserEnterprisePolicies) -> list:
    import capo_bedrock_agentcore_control.types.browser_enterprise_policy

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.browser_enterprise_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BrowserEnterprisePolicies:
    import capo_bedrock_agentcore_control.types.browser_enterprise_policy

    out: BrowserEnterprisePolicies = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.browser_enterprise_policy.deserialize_json(
                item
            )
        )
    return out
