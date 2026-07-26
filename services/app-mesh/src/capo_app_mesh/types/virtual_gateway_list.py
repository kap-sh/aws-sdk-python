"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_ref

VirtualGatewayList: TypeAlias = list[
    "capo_app_mesh.types.virtual_gateway_ref.VirtualGatewayRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayList) -> list:
    import capo_app_mesh.types.virtual_gateway_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.virtual_gateway_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualGatewayList:
    import capo_app_mesh.types.virtual_gateway_ref

    out: VirtualGatewayList = []
    for item in data:
        out.append(capo_app_mesh.types.virtual_gateway_ref.deserialize_json(item))
    return out
