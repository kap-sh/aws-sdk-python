"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteConfigurationBundleRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id

class DeleteConfigurationBundleRequest(TypedDict):
    bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationBundleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationBundleRequest:
    out: DeleteConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
    return out