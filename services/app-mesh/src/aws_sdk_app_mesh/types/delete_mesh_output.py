"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteMeshOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.mesh_data


class DeleteMeshOutput(TypedDict):
    mesh: "aws_sdk_app_mesh.types.mesh_data.MeshData"
    """<p>The service mesh that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMeshOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.mesh_data

    out["mesh"] = aws_sdk_app_mesh.types.mesh_data.serialize_json(value["mesh"])
    return out


def deserialize_json(data: dict) -> DeleteMeshOutput:
    out: DeleteMeshOutput = {}  # type: ignore[typeddict-item]
    if "mesh" in data:
        import aws_sdk_app_mesh.types.mesh_data

        out["mesh"] = aws_sdk_app_mesh.types.mesh_data.deserialize_json(data["mesh"])
    else:
        raise DeserializationError("DeleteMeshOutput.mesh required")
    return out
