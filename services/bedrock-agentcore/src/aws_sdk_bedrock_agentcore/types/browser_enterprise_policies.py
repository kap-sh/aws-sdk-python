"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserEnterprisePolicies``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.browser_enterprise_policy

BrowserEnterprisePolicies: TypeAlias = list["aws_sdk_bedrock_agentcore.types.browser_enterprise_policy.BrowserEnterprisePolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserEnterprisePolicies) -> list:
    import aws_sdk_bedrock_agentcore.types.browser_enterprise_policy
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.browser_enterprise_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrowserEnterprisePolicies:
    import aws_sdk_bedrock_agentcore.types.browser_enterprise_policy
    out: BrowserEnterprisePolicies = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.browser_enterprise_policy.deserialize_json(item))
    return out