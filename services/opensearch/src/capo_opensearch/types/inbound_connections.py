"""Generated from Smithy shape ``com.amazonaws.opensearch#InboundConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.inbound_connection

InboundConnections: TypeAlias = list[
    "capo_opensearch.types.inbound_connection.InboundConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: InboundConnections) -> list:
    import capo_opensearch.types.inbound_connection

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.inbound_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> InboundConnections:
    import capo_opensearch.types.inbound_connection

    out: InboundConnections = []
    for item in data:
        out.append(capo_opensearch.types.inbound_connection.deserialize_json(item))
    return out
