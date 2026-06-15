"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserEnterprisePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policy_type
    import aws_sdk_bedrock_agentcore_control.types.resource_location


class BrowserEnterprisePolicy(TypedDict):
    location: (
        "aws_sdk_bedrock_agentcore_control.types.resource_location.ResourceLocation"
    )
    """<p>The location of the enterprise policy file.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policy_type.BrowserEnterprisePolicyType"
    ]
    """<p>The type of browser enterprise policy. Available values are <code>MANAGED</code> and <code>RECOMMENDED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserEnterprisePolicy) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.resource_location

    out["location"] = (
        aws_sdk_bedrock_agentcore_control.types.resource_location.serialize_json(
            value["location"]
        )
    )
    if "type" in value:
        import aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policy_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policy_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserEnterprisePolicy:
    out: BrowserEnterprisePolicy = {}  # type: ignore[typeddict-item]
    if "location" in data:
        import aws_sdk_bedrock_agentcore_control.types.resource_location

        out["location"] = (
            aws_sdk_bedrock_agentcore_control.types.resource_location.deserialize_json(
                data["location"]
            )
        )
    else:
        raise DeserializationError("BrowserEnterprisePolicy.location required")
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policy_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_enterprise_policy_type.deserialize_json(
                data["type"]
            )
        )
    return out
