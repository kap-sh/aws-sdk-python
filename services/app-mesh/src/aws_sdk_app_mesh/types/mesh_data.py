"""Generated from Smithy shape ``com.amazonaws.appmesh#MeshData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.mesh_spec
    import aws_sdk_app_mesh.types.mesh_status
    import aws_sdk_app_mesh.types.resource_metadata
    import aws_sdk_app_mesh.types.resource_name


class MeshData(TypedDict):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh.</p>"""
    spec: "aws_sdk_app_mesh.types.mesh_spec.MeshSpec"
    """<p>The associated specification for the service mesh.</p>"""
    metadata: "aws_sdk_app_mesh.types.resource_metadata.ResourceMetadata"
    """<p>The associated metadata for the service mesh.</p>"""
    status: "aws_sdk_app_mesh.types.mesh_status.MeshStatus"
    """<p>The status of the service mesh.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeshData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    import aws_sdk_app_mesh.types.mesh_spec

    out["spec"] = aws_sdk_app_mesh.types.mesh_spec.serialize_json(value["spec"])
    import aws_sdk_app_mesh.types.resource_metadata

    out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import aws_sdk_app_mesh.types.mesh_status

    out["status"] = aws_sdk_app_mesh.types.mesh_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> MeshData:
    out: MeshData = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("MeshData.mesh_name required")
    if "spec" in data:
        import aws_sdk_app_mesh.types.mesh_spec

        out["spec"] = aws_sdk_app_mesh.types.mesh_spec.deserialize_json(data["spec"])
    else:
        raise DeserializationError("MeshData.spec required")
    if "metadata" in data:
        import aws_sdk_app_mesh.types.resource_metadata

        out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("MeshData.metadata required")
    if "status" in data:
        import aws_sdk_app_mesh.types.mesh_status

        out["status"] = aws_sdk_app_mesh.types.mesh_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("MeshData.status required")
    return out
