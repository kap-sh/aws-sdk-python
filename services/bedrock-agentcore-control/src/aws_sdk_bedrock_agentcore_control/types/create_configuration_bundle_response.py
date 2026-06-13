"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateConfigurationBundleResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version
    import datetime

class CreateConfigurationBundleResponse(TypedDict):
    bundle_arn: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the created configuration bundle.</p>"""
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the created configuration bundle.</p>"""
    version_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The initial version identifier of the configuration bundle.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the configuration bundle was created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationBundleResponse) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["versionId"] = value["version_id"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationBundleResponse:
    out: CreateConfigurationBundleResponse = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError("CreateConfigurationBundleResponse.bundle_arn required")
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("CreateConfigurationBundleResponse.bundle_id required")
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("CreateConfigurationBundleResponse.version_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateConfigurationBundleResponse.created_at required")
    return out