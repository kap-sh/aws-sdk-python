"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetManifest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list


class AutomatedReasoningPolicyBuildResultAssetManifest(TypedDict):
    entries: "aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.AutomatedReasoningPolicyBuildResultAssetManifestList"
    """<p>The list of asset entries in the manifest, each describing an available artifact that can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetManifest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list

    out["entries"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildResultAssetManifest:
    out: AutomatedReasoningPolicyBuildResultAssetManifest = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list

        out["entries"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildResultAssetManifest.entries required"
        )
    return out
