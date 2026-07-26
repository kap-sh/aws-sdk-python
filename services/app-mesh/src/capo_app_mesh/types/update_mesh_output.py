"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateMeshOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.mesh_data


class UpdateMeshOutput(TypedDict, closed=True):
    mesh: "capo_app_mesh.types.mesh_data.MeshData"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMeshOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.mesh_data

    out["mesh"] = capo_app_mesh.types.mesh_data.serialize_json(value["mesh"])
    return out


def deserialize_json(data: dict) -> UpdateMeshOutput:
    out: UpdateMeshOutput = {}  # type: ignore[typeddict-item]
    if "mesh" in data:
        import capo_app_mesh.types.mesh_data

        out["mesh"] = capo_app_mesh.types.mesh_data.deserialize_json(data["mesh"])
    else:
        raise DeserializationError("UpdateMeshOutput.mesh required")
    return out
