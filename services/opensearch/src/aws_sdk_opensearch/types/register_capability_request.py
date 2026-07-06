"""Generated from Smithy shape ``com.amazonaws.opensearch#RegisterCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.application_id
    import aws_sdk_opensearch.types.capability_base_request_config
    import aws_sdk_opensearch.types.capability_name


class RegisterCapabilityRequest(TypedDict, closed=True):
    application_id: "aws_sdk_opensearch.types.application_id.ApplicationId"
    """<p>The unique identifier of the OpenSearch UI application to register the capability for.</p>"""
    capability_name: "aws_sdk_opensearch.types.capability_name.CapabilityName"
    """<p>The name of the capability to register. Must be between 3 and 30 characters and contain only alphanumeric characters and hyphens. This identifies the type of capability being enabled for the application. For registering AI Assistant capability, use <code>ai-capability</code> </p>"""
    capability_config: "aws_sdk_opensearch.types.capability_base_request_config.CapabilityBaseRequestConfig"
    """<p>The configuration settings for the capability being registered. This includes capability-specific settings such as AI configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCapabilityRequest) -> dict:
    out: dict = {}
    out["capabilityName"] = value["capability_name"]
    import aws_sdk_opensearch.types.capability_base_request_config

    out["capabilityConfig"] = (
        aws_sdk_opensearch.types.capability_base_request_config.serialize_json(
            value["capability_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisterCapabilityRequest:
    out: RegisterCapabilityRequest = {}  # type: ignore[typeddict-item]
    if "capabilityName" in data:
        out["capability_name"] = data["capabilityName"]
    else:
        raise DeserializationError("RegisterCapabilityRequest.capability_name required")
    if "capabilityConfig" in data:
        import aws_sdk_opensearch.types.capability_base_request_config

        out["capability_config"] = (
            aws_sdk_opensearch.types.capability_base_request_config.deserialize_json(
                data["capabilityConfig"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterCapabilityRequest.capability_config required"
        )
    return out
