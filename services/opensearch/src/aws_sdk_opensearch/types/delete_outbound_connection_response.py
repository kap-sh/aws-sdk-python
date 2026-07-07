"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteOutboundConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.outbound_connection


class DeleteOutboundConnectionResponse(TypedDict, closed=True):
    connection: NotRequired[
        "aws_sdk_opensearch.types.outbound_connection.OutboundConnection"
    ]
    """<p>The deleted inbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutboundConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_opensearch.types.outbound_connection

        out["Connection"] = aws_sdk_opensearch.types.outbound_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> DeleteOutboundConnectionResponse:
    out: DeleteOutboundConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_opensearch.types.outbound_connection

        out["connection"] = (
            aws_sdk_opensearch.types.outbound_connection.deserialize_json(
                data["Connection"]
            )
        )
    return out
