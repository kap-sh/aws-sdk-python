"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeVirtualNodeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_node_data


class DescribeVirtualNodeOutput(TypedDict):
    virtual_node: "aws_sdk_app_mesh.types.virtual_node_data.VirtualNodeData"
    """<p>The full description of your virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVirtualNodeOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_node_data

    out["virtualNode"] = aws_sdk_app_mesh.types.virtual_node_data.serialize_json(
        value["virtual_node"]
    )
    return out


def deserialize_json(data: dict) -> DescribeVirtualNodeOutput:
    out: DescribeVirtualNodeOutput = {}  # type: ignore[typeddict-item]
    if "virtualNode" in data:
        import aws_sdk_app_mesh.types.virtual_node_data

        out["virtual_node"] = aws_sdk_app_mesh.types.virtual_node_data.deserialize_json(
            data["virtualNode"]
        )
    else:
        raise DeserializationError("DescribeVirtualNodeOutput.virtual_node required")
    return out
