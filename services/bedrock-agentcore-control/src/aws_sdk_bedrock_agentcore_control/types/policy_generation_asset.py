"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.findings
    import aws_sdk_bedrock_agentcore_control.types.natural_language
    import aws_sdk_bedrock_agentcore_control.types.policy_definition
    import aws_sdk_bedrock_agentcore_control.types.resource_id


class PolicyGenerationAsset(TypedDict, closed=True):
    policy_generation_asset_id: (
        "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier for this generated policy asset within the policy generation request. This ID can be used to reference specific generated policy options when creating actual policies from the generation results.</p>"""
    definition: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    ]
    raw_text_fragment: (
        "aws_sdk_bedrock_agentcore_control.types.natural_language.NaturalLanguage"
    )
    """<p>The portion of the original natural language input that this generated policy asset addresses. This helps users understand which part of their policy description was translated into this specific Cedar policy statement, enabling better policy selection and refinement. When a single natural language input describes multiple authorization requirements, the generation process creates separate policy assets for each requirement, with each asset's rawTextFragment showing which requirement it addresses. Use this mapping to verify that all parts of your natural language input were correctly translated into Cedar policies.</p>"""
    findings: "aws_sdk_bedrock_agentcore_control.types.findings.Findings"
    """<p>Analysis findings and insights related to this specific generated policy asset. These findings may include validation results, potential issues, or recommendations for improvement to help users evaluate the quality and appropriateness of the generated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationAsset) -> dict:
    out: dict = {}
    out["policyGenerationAssetId"] = value["policy_generation_asset_id"]
    if "definition" in value:
        import aws_sdk_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_definition.serialize_json(
                value["definition"]
            )
        )
    out["rawTextFragment"] = value["raw_text_fragment"]
    import aws_sdk_bedrock_agentcore_control.types.findings

    out["findings"] = aws_sdk_bedrock_agentcore_control.types.findings.serialize_json(
        value["findings"]
    )
    return out


def deserialize_json(data: dict) -> PolicyGenerationAsset:
    out: PolicyGenerationAsset = {}  # type: ignore[typeddict-item]
    if "policyGenerationAssetId" in data:
        out["policy_generation_asset_id"] = data["policyGenerationAssetId"]
    else:
        raise DeserializationError(
            "PolicyGenerationAsset.policy_generation_asset_id required"
        )
    if "definition" in data:
        import aws_sdk_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            aws_sdk_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    if "rawTextFragment" in data:
        out["raw_text_fragment"] = data["rawTextFragment"]
    else:
        raise DeserializationError("PolicyGenerationAsset.raw_text_fragment required")
    if "findings" in data:
        import aws_sdk_bedrock_agentcore_control.types.findings

        out["findings"] = (
            aws_sdk_bedrock_agentcore_control.types.findings.deserialize_json(
                data["findings"]
            )
        )
    else:
        raise DeserializationError("PolicyGenerationAsset.findings required")
    return out
