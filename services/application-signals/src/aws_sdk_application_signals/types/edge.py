"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Edge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.connection_type


class Edge(TypedDict, closed=True):
    source_node_id: NotRequired["str"]
    """<p>The identifier of the source node in this edge connection.</p>"""
    destination_node_id: NotRequired["str"]
    """<p>The identifier of the destination node in this edge connection.</p>"""
    duration: NotRequired["float"]
    """<p>The duration or latency associated with this connection, if applicable.</p>"""
    connection_type: NotRequired[
        "aws_sdk_application_signals.types.connection_type.ConnectionType"
    ]
    """<p>The type of connection between the nodes, indicating the nature of the relationship.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Edge) -> dict:
    out: dict = {}
    if "source_node_id" in value:
        out["SourceNodeId"] = value["source_node_id"]
    if "destination_node_id" in value:
        out["DestinationNodeId"] = value["destination_node_id"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "connection_type" in value:
        import aws_sdk_application_signals.types.connection_type

        out["ConnectionType"] = (
            aws_sdk_application_signals.types.connection_type.serialize_json(
                value["connection_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> Edge:
    out: Edge = {}  # type: ignore[typeddict-item]
    if "SourceNodeId" in data:
        out["source_node_id"] = data["SourceNodeId"]
    if "DestinationNodeId" in data:
        out["destination_node_id"] = data["DestinationNodeId"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "ConnectionType" in data:
        import aws_sdk_application_signals.types.connection_type

        out["connection_type"] = (
            aws_sdk_application_signals.types.connection_type.deserialize_json(
                data["ConnectionType"]
            )
        )
    return out
