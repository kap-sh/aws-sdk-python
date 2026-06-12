"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeMeshOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.mesh_data

class DescribeMeshOutput(TypedDict):
    mesh: "aws_sdk_app_mesh.types.mesh_data.MeshData"
    """<p>The full description of your service mesh.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeMeshOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.mesh_data
    out["mesh"] = aws_sdk_app_mesh.types.mesh_data.serialize_json(value["mesh"])
    return out


def deserialize_json(data: dict) -> DescribeMeshOutput:
    out: DescribeMeshOutput = {}  # type: ignore[typeddict-item]
    if "mesh" in data:
        import aws_sdk_app_mesh.types.mesh_data
        out["mesh"] = aws_sdk_app_mesh.types.mesh_data.deserialize_json(data["mesh"])
    else:
        raise DeserializationError("DescribeMeshOutput.mesh required")
    return out