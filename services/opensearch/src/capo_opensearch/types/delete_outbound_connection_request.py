"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteOutboundConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.connection_id


class DeleteOutboundConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_opensearch.types.connection_id.ConnectionId"
    """<p>The ID of the outbound connection you want to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutboundConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOutboundConnectionRequest:
    out: DeleteOutboundConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
