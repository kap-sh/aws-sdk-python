"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationAssetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_assets


class ListPolicyGenerationAssetsResponse(TypedDict):
    policy_generation_assets: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.policy_generation_assets.PolicyGenerationAssets"
    ]
    """<p>An array of generated policy assets including Cedar policies and related artifacts from the AI-powered policy generation process. Each asset represents a different policy option or variation generated from the original natural language input.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    r"""<p>A pagination token that can be used in subsequent <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html\">ListPolicyGenerationAssets</a> calls to retrieve additional assets. This token is only present when there are more generated policy assets available beyond the current response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationAssetsResponse) -> dict:
    out: dict = {}
    if "policy_generation_assets" in value:
        import aws_sdk_bedrock_agentcore_control.types.policy_generation_assets

        out["policyGenerationAssets"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_generation_assets.serialize_json(
                value["policy_generation_assets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationAssetsResponse:
    out: ListPolicyGenerationAssetsResponse = {}  # type: ignore[typeddict-item]
    if "policyGenerationAssets" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_generation_assets

        out["policy_generation_assets"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_generation_assets.deserialize_json(
                data["policyGenerationAssets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
