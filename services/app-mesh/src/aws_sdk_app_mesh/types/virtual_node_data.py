"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_metadata
    import aws_sdk_app_mesh.types.resource_name
    import aws_sdk_app_mesh.types.virtual_node_spec
    import aws_sdk_app_mesh.types.virtual_node_status


class VirtualNodeData(TypedDict, closed=True):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual node resides in.</p>"""
    virtual_node_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual node.</p>"""
    spec: "aws_sdk_app_mesh.types.virtual_node_spec.VirtualNodeSpec"
    """<p>The specifications of the virtual node.</p>"""
    metadata: "aws_sdk_app_mesh.types.resource_metadata.ResourceMetadata"
    """<p>The associated metadata for the virtual node.</p>"""
    status: "aws_sdk_app_mesh.types.virtual_node_status.VirtualNodeStatus"
    """<p>The current status for the virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualNodeName"] = value["virtual_node_name"]
    import aws_sdk_app_mesh.types.virtual_node_spec

    out["spec"] = aws_sdk_app_mesh.types.virtual_node_spec.serialize_json(value["spec"])
    import aws_sdk_app_mesh.types.resource_metadata

    out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import aws_sdk_app_mesh.types.virtual_node_status

    out["status"] = aws_sdk_app_mesh.types.virtual_node_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VirtualNodeData:
    out: VirtualNodeData = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("VirtualNodeData.mesh_name required")
    if "virtualNodeName" in data:
        out["virtual_node_name"] = data["virtualNodeName"]
    else:
        raise DeserializationError("VirtualNodeData.virtual_node_name required")
    if "spec" in data:
        import aws_sdk_app_mesh.types.virtual_node_spec

        out["spec"] = aws_sdk_app_mesh.types.virtual_node_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("VirtualNodeData.spec required")
    if "metadata" in data:
        import aws_sdk_app_mesh.types.resource_metadata

        out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("VirtualNodeData.metadata required")
    if "status" in data:
        import aws_sdk_app_mesh.types.virtual_node_status

        out["status"] = aws_sdk_app_mesh.types.virtual_node_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("VirtualNodeData.status required")
    return out
