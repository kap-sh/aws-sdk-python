"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_listener

VirtualGatewayListeners: TypeAlias = list[
    "capo_app_mesh.types.virtual_gateway_listener.VirtualGatewayListener"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListeners) -> list:
    import capo_app_mesh.types.virtual_gateway_listener

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.virtual_gateway_listener.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualGatewayListeners:
    import capo_app_mesh.types.virtual_gateway_listener

    out: VirtualGatewayListeners = []
    for item in data:
        out.append(capo_app_mesh.types.virtual_gateway_listener.deserialize_json(item))
    return out
