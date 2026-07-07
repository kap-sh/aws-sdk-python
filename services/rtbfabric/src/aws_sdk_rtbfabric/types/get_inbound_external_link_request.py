"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetInboundExternalLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id


class GetInboundExternalLinkRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInboundExternalLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInboundExternalLinkRequest:
    out: GetInboundExternalLinkRequest = {}  # type: ignore[typeddict-item]
    return out
