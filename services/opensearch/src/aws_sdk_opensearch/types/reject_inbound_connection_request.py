"""Generated from Smithy shape ``com.amazonaws.opensearch#RejectInboundConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.connection_id


class RejectInboundConnectionRequest(TypedDict):
    connection_id: "aws_sdk_opensearch.types.connection_id.ConnectionId"
    """<p>The unique identifier of the inbound connection to reject.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectInboundConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectInboundConnectionRequest:
    out: RejectInboundConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
