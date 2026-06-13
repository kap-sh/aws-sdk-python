"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_listener

VirtualGatewayListeners: TypeAlias = list[
    "aws_sdk_app_mesh.types.virtual_gateway_listener.VirtualGatewayListener"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListeners) -> list:
    import aws_sdk_app_mesh.types.virtual_gateway_listener

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.virtual_gateway_listener.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualGatewayListeners:
    import aws_sdk_app_mesh.types.virtual_gateway_listener

    out: VirtualGatewayListeners = []
    for item in data:
        out.append(
            aws_sdk_app_mesh.types.virtual_gateway_listener.deserialize_json(item)
        )
    return out
