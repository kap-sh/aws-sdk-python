"""Generated from Smithy shape ``com.amazonaws.opensearch#RegisterCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_id
    import capo_opensearch.types.capability_base_response_config
    import capo_opensearch.types.capability_name
    import capo_opensearch.types.capability_status


class RegisterCapabilityResponse(TypedDict, closed=True):
    capability_name: NotRequired["capo_opensearch.types.capability_name.CapabilityName"]
    """<p>The name of the registered capability.</p>"""
    application_id: NotRequired["capo_opensearch.types.application_id.ApplicationId"]
    """<p>The unique identifier of the OpenSearch UI application.</p>"""
    status: NotRequired["capo_opensearch.types.capability_status.CapabilityStatus"]
    """<p>The current status of the capability. Possible values: <code>creating</code>, <code>create_failed</code>, <code>active</code>, <code>updating</code>, <code>update_failed</code>, <code>deleting</code>, <code>delete_failed</code>.</p>"""
    capability_config: NotRequired[
        "capo_opensearch.types.capability_base_response_config.CapabilityBaseResponseConfig"
    ]
    """<p>The configuration settings for the registered capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCapabilityResponse) -> dict:
    out: dict = {}
    if "capability_name" in value:
        out["capabilityName"] = value["capability_name"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "status" in value:
        import capo_opensearch.types.capability_status

        out["status"] = capo_opensearch.types.capability_status.serialize_json(
            value["status"]
        )
    if "capability_config" in value:
        import capo_opensearch.types.capability_base_response_config

        out["capabilityConfig"] = (
            capo_opensearch.types.capability_base_response_config.serialize_json(
                value["capability_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterCapabilityResponse:
    out: RegisterCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capabilityName" in data:
        out["capability_name"] = data["capabilityName"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "status" in data:
        import capo_opensearch.types.capability_status

        out["status"] = capo_opensearch.types.capability_status.deserialize_json(
            data["status"]
        )
    if "capabilityConfig" in data:
        import capo_opensearch.types.capability_base_response_config

        out["capability_config"] = (
            capo_opensearch.types.capability_base_response_config.deserialize_json(
                data["capabilityConfig"]
            )
        )
    return out
