"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteOutboundConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.connection_id


class DeleteOutboundConnectionRequest(TypedDict):
    connection_id: "aws_sdk_opensearch.types.connection_id.ConnectionId"
    """<p>The ID of the outbound connection you want to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutboundConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOutboundConnectionRequest:
    out: DeleteOutboundConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
