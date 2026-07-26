"""Generated from Smithy shape ``com.amazonaws.opensearch#GetCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_id
    import capo_opensearch.types.capability_name


class GetCapabilityRequest(TypedDict, closed=True):
    application_id: "capo_opensearch.types.application_id.ApplicationId"
    """<p>The unique identifier of the OpenSearch UI application.</p>"""
    capability_name: "capo_opensearch.types.capability_name.CapabilityName"
    """<p>The name of the capability to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapabilityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCapabilityRequest:
    out: GetCapabilityRequest = {}  # type: ignore[typeddict-item]
    return out
