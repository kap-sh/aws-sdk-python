"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DeletePrivateGraphEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.vpc_id


class DeletePrivateGraphEndpointInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    vpc_id: "aws_sdk_neptune_graph.types.vpc_id.VpcId"
    """<p>The ID of the VPC where the private endpoint is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateGraphEndpointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePrivateGraphEndpointInput:
    out: DeletePrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
    return out
