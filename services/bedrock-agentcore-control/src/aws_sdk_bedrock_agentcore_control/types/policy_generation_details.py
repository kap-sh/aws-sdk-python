"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class PolicyGenerationDetails(TypedDict):
    policy_generation_id: (
        "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier for this policy generation request.</p>"""
    policy_generation_asset_id: (
        "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier for this generated policy asset within the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationDetails) -> dict:
    out: dict = {}
    out["policyGenerationId"] = value["policy_generation_id"]
    out["policyGenerationAssetId"] = value["policy_generation_asset_id"]
    return out


def deserialize_json(data: dict) -> PolicyGenerationDetails:
    out: PolicyGenerationDetails = {}  # type: ignore[typeddict-item]
    if "policyGenerationId" in data:
        out["policy_generation_id"] = data["policyGenerationId"]
    else:
        raise DeserializationError(
            "PolicyGenerationDetails.policy_generation_id required"
        )
    if "policyGenerationAssetId" in data:
        out["policy_generation_asset_id"] = data["policyGenerationAssetId"]
    else:
        raise DeserializationError(
            "PolicyGenerationDetails.policy_generation_asset_id required"
        )
    return out
