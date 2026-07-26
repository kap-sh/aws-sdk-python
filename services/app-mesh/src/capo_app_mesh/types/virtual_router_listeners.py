"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterListeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_listener

VirtualRouterListeners: TypeAlias = list[
    "capo_app_mesh.types.virtual_router_listener.VirtualRouterListener"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterListeners) -> list:
    import capo_app_mesh.types.virtual_router_listener

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.virtual_router_listener.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualRouterListeners:
    import capo_app_mesh.types.virtual_router_listener

    out: VirtualRouterListeners = []
    for item in data:
        out.append(capo_app_mesh.types.virtual_router_listener.deserialize_json(item))
    return out
