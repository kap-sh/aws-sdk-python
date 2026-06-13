"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id


class GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow assets you want to retrieve.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow whose result assets you want to retrieve.</p>"""
    asset_type: "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type.AutomatedReasoningPolicyBuildResultAssetType"
    """<p>The type of asset to retrieve (e.g., BUILD_LOG, QUALITY_REPORT, POLICY_DEFINITION, GENERATED_TEST_CASES, POLICY_SCENARIOS, FIDELITY_REPORT, ASSET_MANIFEST, SOURCE_DOCUMENT).</p>"""
    asset_id: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_id.AutomatedReasoningPolicyBuildResultAssetId"
    ]
    """<p>The unique identifier of the specific asset to retrieve when multiple assets of the same type exist. This is required when retrieving SOURCE_DOCUMENT assets, as multiple source documents may have been used in the workflow. The asset ID can be obtained from the asset manifest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest:
    out: GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest = {}  # type: ignore[typeddict-item]
    return out
