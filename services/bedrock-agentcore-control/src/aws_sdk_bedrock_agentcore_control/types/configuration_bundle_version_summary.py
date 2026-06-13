"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version
    import aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata
    import datetime

class ConfigurationBundleVersionSummary(TypedDict):
    bundle_arn: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle.</p>"""
    version_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The version identifier of this configuration bundle version.</p>"""
    lineage_metadata: NotRequired["aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata.VersionLineageMetadata"]
    """<p>The version lineage metadata, including parent versions, branch name, and creation source.</p>"""
    version_created_at: "datetime.datetime"
    """<p>The timestamp when this version was created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleVersionSummary) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["versionId"] = value["version_id"]
    if "lineage_metadata" in value:
        import aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata
        out["lineageMetadata"] = aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata.serialize_json(value["lineage_metadata"])
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["versionCreatedAt"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["version_created_at"])
    return out


def deserialize_json(data: dict) -> ConfigurationBundleVersionSummary:
    out: ConfigurationBundleVersionSummary = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError("ConfigurationBundleVersionSummary.bundle_arn required")
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("ConfigurationBundleVersionSummary.bundle_id required")
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("ConfigurationBundleVersionSummary.version_id required")
    if "lineageMetadata" in data:
        import aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata
        out["lineage_metadata"] = aws_sdk_bedrock_agentcore_control.types.version_lineage_metadata.deserialize_json(data["lineageMetadata"])
    if "versionCreatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["version_created_at"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["versionCreatedAt"])
    else:
        raise DeserializationError("ConfigurationBundleVersionSummary.version_created_at required")
    return out