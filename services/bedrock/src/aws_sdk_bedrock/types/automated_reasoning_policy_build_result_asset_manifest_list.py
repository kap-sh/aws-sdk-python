"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetManifestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

AutomatedReasoningPolicyBuildResultAssetManifestList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.AutomatedReasoningPolicyBuildResultAssetManifestEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetManifestList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AutomatedReasoningPolicyBuildResultAssetManifestList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

    out: AutomatedReasoningPolicyBuildResultAssetManifestList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.deserialize_json(
                item
            )
        )
    return out
