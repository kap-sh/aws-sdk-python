"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterListeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_router_listener

VirtualRouterListeners: TypeAlias = list[
    "aws_sdk_app_mesh.types.virtual_router_listener.VirtualRouterListener"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterListeners) -> list:
    import aws_sdk_app_mesh.types.virtual_router_listener

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.virtual_router_listener.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualRouterListeners:
    import aws_sdk_app_mesh.types.virtual_router_listener

    out: VirtualRouterListeners = []
    for item in data:
        out.append(
            aws_sdk_app_mesh.types.virtual_router_listener.deserialize_json(item)
        )
    return out
