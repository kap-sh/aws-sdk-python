"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateOutboundExternalLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.link_status


class CreateOutboundExternalLinkResponse(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "aws_sdk_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutboundExternalLinkResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["linkId"] = value["link_id"]
    import aws_sdk_rtbfabric.types.link_status

    out["status"] = aws_sdk_rtbfabric.types.link_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateOutboundExternalLinkResponse:
    out: CreateOutboundExternalLinkResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError(
            "CreateOutboundExternalLinkResponse.gateway_id required"
        )
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError(
            "CreateOutboundExternalLinkResponse.link_id required"
        )
    if "status" in data:
        import aws_sdk_rtbfabric.types.link_status

        out["status"] = aws_sdk_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateOutboundExternalLinkResponse.status required")
    return out
