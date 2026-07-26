"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_node_ref

VirtualNodeList: TypeAlias = list["capo_app_mesh.types.virtual_node_ref.VirtualNodeRef"]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeList) -> list:
    import capo_app_mesh.types.virtual_node_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.virtual_node_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualNodeList:
    import capo_app_mesh.types.virtual_node_ref

    out: VirtualNodeList = []
    for item in data:
        out.append(capo_app_mesh.types.virtual_node_ref.deserialize_json(item))
    return out
