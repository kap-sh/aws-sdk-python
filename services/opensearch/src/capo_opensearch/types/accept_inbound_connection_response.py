"""Generated from Smithy shape ``com.amazonaws.opensearch#AcceptInboundConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.inbound_connection


class AcceptInboundConnectionResponse(TypedDict, closed=True):
    connection: NotRequired[
        "capo_opensearch.types.inbound_connection.InboundConnection"
    ]
    """<p>Information about the accepted inbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInboundConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_opensearch.types.inbound_connection

        out["Connection"] = capo_opensearch.types.inbound_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> AcceptInboundConnectionResponse:
    out: AcceptInboundConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import capo_opensearch.types.inbound_connection

        out["connection"] = capo_opensearch.types.inbound_connection.deserialize_json(
            data["Connection"]
        )
    return out
