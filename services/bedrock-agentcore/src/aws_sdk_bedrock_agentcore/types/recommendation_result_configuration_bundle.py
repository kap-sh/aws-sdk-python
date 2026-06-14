"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationResultConfigurationBundle``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_arn
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_version_id


class RecommendationResultConfigurationBundle(TypedDict):
    bundle_arn: "aws_sdk_bedrock_agentcore.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    version_id: "aws_sdk_bedrock_agentcore.types.configuration_bundle_version_id.ConfigurationBundleVersionId"
    """<p>The version identifier of the configuration bundle containing the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResultConfigurationBundle) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> RecommendationResultConfigurationBundle:
    out: RecommendationResultConfigurationBundle = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError(
            "RecommendationResultConfigurationBundle.bundle_arn required"
        )
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError(
            "RecommendationResultConfigurationBundle.version_id required"
        )
    return out
