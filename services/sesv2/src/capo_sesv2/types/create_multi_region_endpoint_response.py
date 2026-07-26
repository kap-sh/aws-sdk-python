"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateMultiRegionEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.endpoint_id
    import capo_sesv2.types.status


class CreateMultiRegionEndpointResponse(TypedDict, closed=True):
    status: NotRequired["capo_sesv2.types.status.Status"]
    """<p>A status of the multi-region endpoint (global-endpoint) right after the create request.</p> <ul> <li> <p> <code>CREATING</code> – The resource is being provisioned.</p> </li> <li> <p> <code>READY</code> – The resource is ready to use.</p> </li> <li> <p> <code>FAILED</code> – The resource failed to be provisioned.</p> </li> <li> <p> <code>DELETING</code> – The resource is being deleted as requested.</p> </li> </ul>"""
    endpoint_id: NotRequired["capo_sesv2.types.endpoint_id.EndpointId"]
    """<p>The ID of the multi-region endpoint (global-endpoint).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiRegionEndpointResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sesv2.types.status

        out["Status"] = capo_sesv2.types.status.serialize_json(value["status"])
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    return out


def deserialize_json(data: dict) -> CreateMultiRegionEndpointResponse:
    out: CreateMultiRegionEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_sesv2.types.status

        out["status"] = capo_sesv2.types.status.deserialize_json(data["Status"])
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    return out
