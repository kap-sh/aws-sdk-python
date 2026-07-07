"""Generated from Smithy shape ``com.amazonaws.opensearch#DeregisterCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.application_id
    import aws_sdk_opensearch.types.capability_name


class DeregisterCapabilityRequest(TypedDict, closed=True):
    application_id: "aws_sdk_opensearch.types.application_id.ApplicationId"
    """<p>The unique identifier of the OpenSearch UI application to deregister the capability from.</p>"""
    capability_name: "aws_sdk_opensearch.types.capability_name.CapabilityName"
    """<p>The name of the capability to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterCapabilityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterCapabilityRequest:
    out: DeregisterCapabilityRequest = {}  # type: ignore[typeddict-item]
    return out
