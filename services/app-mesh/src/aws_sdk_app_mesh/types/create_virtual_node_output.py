"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateVirtualNodeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_node_data

class CreateVirtualNodeOutput(TypedDict):
    virtual_node: "aws_sdk_app_mesh.types.virtual_node_data.VirtualNodeData"
    """<p>The full description of your virtual node following the create call.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualNodeOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_node_data
    out["virtualNode"] = aws_sdk_app_mesh.types.virtual_node_data.serialize_json(value["virtual_node"])
    return out


def deserialize_json(data: dict) -> CreateVirtualNodeOutput:
    out: CreateVirtualNodeOutput = {}  # type: ignore[typeddict-item]
    if "virtualNode" in data:
        import aws_sdk_app_mesh.types.virtual_node_data
        out["virtual_node"] = aws_sdk_app_mesh.types.virtual_node_data.deserialize_json(data["virtualNode"])
    else:
        raise DeserializationError("CreateVirtualNodeOutput.virtual_node required")
    return out