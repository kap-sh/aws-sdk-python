"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteConfigurationBundleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_status


class DeleteConfigurationBundleResponse(TypedDict, closed=True):
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the deleted configuration bundle.</p>"""
    status: "capo_bedrock_agentcore_control.types.configuration_bundle_status.ConfigurationBundleStatus"
    """<p>The status of the configuration bundle deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationBundleResponse) -> dict:
    out: dict = {}
    out["bundleId"] = value["bundle_id"]
    import capo_bedrock_agentcore_control.types.configuration_bundle_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.configuration_bundle_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteConfigurationBundleResponse:
    out: DeleteConfigurationBundleResponse = {}  # type: ignore[typeddict-item]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError(
            "DeleteConfigurationBundleResponse.bundle_id required"
        )
    if "status" in data:
        import capo_bedrock_agentcore_control.types.configuration_bundle_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteConfigurationBundleResponse.status required")
    return out
