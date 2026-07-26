"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_ref

VirtualRouterList: TypeAlias = list[
    "capo_app_mesh.types.virtual_router_ref.VirtualRouterRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterList) -> list:
    import capo_app_mesh.types.virtual_router_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.virtual_router_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualRouterList:
    import capo_app_mesh.types.virtual_router_ref

    out: VirtualRouterList = []
    for item in data:
        out.append(capo_app_mesh.types.virtual_router_ref.deserialize_json(item))
    return out
