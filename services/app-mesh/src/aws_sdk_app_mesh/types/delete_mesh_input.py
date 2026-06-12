"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteMeshInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_name

class DeleteMeshInput(TypedDict):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteMeshInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMeshInput:
    out: DeleteMeshInput = {}  # type: ignore[typeddict-item]
    return out