"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateInboundExternalLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_status


class CreateInboundExternalLinkResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the request.</p>"""
    domain_name: "capo_rtbfabric.types.domain_name.DomainName"
    """<p>The domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInboundExternalLinkResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["linkId"] = value["link_id"]
    import capo_rtbfabric.types.link_status

    out["status"] = capo_rtbfabric.types.link_status.serialize_json(value["status"])
    out["domainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> CreateInboundExternalLinkResponse:
    out: CreateInboundExternalLinkResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError(
            "CreateInboundExternalLinkResponse.gateway_id required"
        )
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("CreateInboundExternalLinkResponse.link_id required")
    if "status" in data:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateInboundExternalLinkResponse.status required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError(
            "CreateInboundExternalLinkResponse.domain_name required"
        )
    return out
