"""Generated from Smithy shape ``com.amazonaws.appmesh#MeshList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.mesh_ref

MeshList: TypeAlias = list["aws_sdk_app_mesh.types.mesh_ref.MeshRef"]


# --- restJson1 ser/de ---
def serialize_json(value: MeshList) -> list:
    import aws_sdk_app_mesh.types.mesh_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.mesh_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> MeshList:
    import aws_sdk_app_mesh.types.mesh_ref

    out: MeshList = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.mesh_ref.deserialize_json(item))
    return out
