"""Generated from Smithy shape ``com.amazonaws.opensearch#RejectInboundConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.inbound_connection


class RejectInboundConnectionResponse(TypedDict, closed=True):
    connection: NotRequired[
        "aws_sdk_opensearch.types.inbound_connection.InboundConnection"
    ]
    """<p>Contains details about the rejected inbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectInboundConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_opensearch.types.inbound_connection

        out["Connection"] = aws_sdk_opensearch.types.inbound_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> RejectInboundConnectionResponse:
    out: RejectInboundConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_opensearch.types.inbound_connection

        out["connection"] = (
            aws_sdk_opensearch.types.inbound_connection.deserialize_json(
                data["Connection"]
            )
        )
    return out
