"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetManifestEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type


class AutomatedReasoningPolicyBuildResultAssetManifestEntry(TypedDict):
    asset_type: "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type.AutomatedReasoningPolicyBuildResultAssetType"
    """<p>The type of asset (e.g., BUILD_LOG, QUALITY_REPORT, POLICY_DEFINITION, GENERATED_TEST_CASES, POLICY_SCENARIOS, FIDELITY_REPORT, ASSET_MANIFEST, SOURCE_DOCUMENT).</p>"""
    asset_name: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_name.AutomatedReasoningPolicyBuildResultAssetName"
    ]
    """<p>A human-readable name for the asset, if applicable. This helps identify specific documents or reports within the workflow results.</p>"""
    asset_id: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_id.AutomatedReasoningPolicyBuildResultAssetId"
    ]
    """<p>A unique identifier for the asset, if applicable. Use this ID when requesting specific assets through the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyBuildResultAssetManifestEntry,
) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type

    out["assetType"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type.serialize_json(
            value["asset_type"]
        )
    )
    if "asset_name" in value:
        out["assetName"] = value["asset_name"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    return out


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyBuildResultAssetManifestEntry:
    out: AutomatedReasoningPolicyBuildResultAssetManifestEntry = {}  # type: ignore[typeddict-item]
    if "assetType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type

        out["asset_type"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_type.deserialize_json(
                data["assetType"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildResultAssetManifestEntry.asset_type required"
        )
    if "assetName" in data:
        out["asset_name"] = data["assetName"]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    return out
