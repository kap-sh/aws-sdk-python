"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateNodeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class CreateNodeOutput(TypedDict):
    node_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeOutput) -> dict:
    out: dict = {}
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    return out


def deserialize_json(data: dict) -> CreateNodeOutput:
    out: CreateNodeOutput = {}  # type: ignore[typeddict-item]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    return out
