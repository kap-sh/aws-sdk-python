"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteInboundConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.inbound_connection


class DeleteInboundConnectionResponse(TypedDict, closed=True):
    connection: NotRequired[
        "capo_opensearch.types.inbound_connection.InboundConnection"
    ]
    """<p>The deleted inbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInboundConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_opensearch.types.inbound_connection

        out["Connection"] = capo_opensearch.types.inbound_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> DeleteInboundConnectionResponse:
    out: DeleteInboundConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import capo_opensearch.types.inbound_connection

        out["connection"] = capo_opensearch.types.inbound_connection.deserialize_json(
            data["Connection"]
        )
    return out
