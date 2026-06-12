"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteInboundConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.inbound_connection


class DeleteInboundConnectionResponse(TypedDict):
    connection: NotRequired[
        "aws_sdk_opensearch.types.inbound_connection.InboundConnection"
    ]
    """<p>The deleted inbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInboundConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_opensearch.types.inbound_connection

        out["Connection"] = aws_sdk_opensearch.types.inbound_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> DeleteInboundConnectionResponse:
    out: DeleteInboundConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_opensearch.types.inbound_connection

        out["connection"] = (
            aws_sdk_opensearch.types.inbound_connection.deserialize_json(
                data["Connection"]
            )
        )
    return out
