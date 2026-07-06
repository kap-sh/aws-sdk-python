"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteInboundExternalLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id


class DeleteInboundExternalLinkRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInboundExternalLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInboundExternalLinkRequest:
    out: DeleteInboundExternalLinkRequest = {}  # type: ignore[typeddict-item]
    return out
