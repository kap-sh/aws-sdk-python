"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkModuleFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_status


class UpdateLinkModuleFlowResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkModuleFlowResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["linkId"] = value["link_id"]
    import capo_rtbfabric.types.link_status

    out["status"] = capo_rtbfabric.types.link_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> UpdateLinkModuleFlowResponse:
    out: UpdateLinkModuleFlowResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("UpdateLinkModuleFlowResponse.gateway_id required")
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("UpdateLinkModuleFlowResponse.link_id required")
    if "status" in data:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateLinkModuleFlowResponse.status required")
    return out
