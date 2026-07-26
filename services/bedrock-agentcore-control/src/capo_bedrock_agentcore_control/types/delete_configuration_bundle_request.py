"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteConfigurationBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_id


class DeleteConfigurationBundleRequest(TypedDict, closed=True):
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationBundleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationBundleRequest:
    out: DeleteConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
    return out
