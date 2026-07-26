"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteInboundConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.connection_id


class DeleteInboundConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_opensearch.types.connection_id.ConnectionId"
    """<p>The ID of the inbound connection to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInboundConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInboundConnectionRequest:
    out: DeleteInboundConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
