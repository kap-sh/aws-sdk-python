"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_router_ref

VirtualRouterList: TypeAlias = list[
    "aws_sdk_app_mesh.types.virtual_router_ref.VirtualRouterRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterList) -> list:
    import aws_sdk_app_mesh.types.virtual_router_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.virtual_router_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualRouterList:
    import aws_sdk_app_mesh.types.virtual_router_ref

    out: VirtualRouterList = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.virtual_router_ref.deserialize_json(item))
    return out
