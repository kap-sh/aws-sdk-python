"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteOutboundExternalLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id


class DeleteOutboundExternalLinkRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutboundExternalLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOutboundExternalLinkRequest:
    out: DeleteOutboundExternalLinkRequest = {}  # type: ignore[typeddict-item]
    return out
