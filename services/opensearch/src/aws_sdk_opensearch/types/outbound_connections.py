"""Generated from Smithy shape ``com.amazonaws.opensearch#OutboundConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.outbound_connection

OutboundConnections: TypeAlias = list[
    "aws_sdk_opensearch.types.outbound_connection.OutboundConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundConnections) -> list:
    import aws_sdk_opensearch.types.outbound_connection

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.outbound_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutboundConnections:
    import aws_sdk_opensearch.types.outbound_connection

    out: OutboundConnections = []
    for item in data:
        out.append(aws_sdk_opensearch.types.outbound_connection.deserialize_json(item))
    return out
