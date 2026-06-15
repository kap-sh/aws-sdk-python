"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetConfigurationBundleVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version


class GetConfigurationBundleVersionRequest(TypedDict):
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle.</p>"""
    version_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The version identifier of the configuration bundle version to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationBundleVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationBundleVersionRequest:
    out: GetConfigurationBundleVersionRequest = {}  # type: ignore[typeddict-item]
    return out
