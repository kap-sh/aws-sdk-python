"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateRequesterGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.requester_gateway_status


class CreateRequesterGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    domain_name: "capo_rtbfabric.types.domain_name.DomainName"
    """<p>The domain name of the requester gateway.</p>"""
    status: "capo_rtbfabric.types.requester_gateway_status.RequesterGatewayStatus"
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRequesterGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["domainName"] = value["domain_name"]
    import capo_rtbfabric.types.requester_gateway_status

    out["status"] = capo_rtbfabric.types.requester_gateway_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateRequesterGatewayResponse:
    out: CreateRequesterGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("CreateRequesterGatewayResponse.gateway_id required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError(
            "CreateRequesterGatewayResponse.domain_name required"
        )
    if "status" in data:
        import capo_rtbfabric.types.requester_gateway_status

        out["status"] = capo_rtbfabric.types.requester_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateRequesterGatewayResponse.status required")
    return out
