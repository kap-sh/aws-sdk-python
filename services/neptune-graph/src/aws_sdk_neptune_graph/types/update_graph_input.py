"""Generated from Smithy shape ``com.amazonaws.neptunegraph#UpdateGraphInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.provisioned_memory


class UpdateGraphInput(TypedDict):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>"""
    provisioned_memory: NotRequired[
        "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGraphInput) -> dict:
    out: dict = {}
    if "public_connectivity" in value:
        out["publicConnectivity"] = value["public_connectivity"]
    if "provisioned_memory" in value:
        out["provisionedMemory"] = value["provisioned_memory"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_json(data: dict) -> UpdateGraphInput:
    out: UpdateGraphInput = {}  # type: ignore[typeddict-item]
    if "publicConnectivity" in data:
        out["public_connectivity"] = data["publicConnectivity"]
    if "provisionedMemory" in data:
        out["provisioned_memory"] = data["provisionedMemory"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    return out
