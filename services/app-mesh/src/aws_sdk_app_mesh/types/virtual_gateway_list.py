"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_ref

VirtualGatewayList: TypeAlias = list[
    "aws_sdk_app_mesh.types.virtual_gateway_ref.VirtualGatewayRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayList) -> list:
    import aws_sdk_app_mesh.types.virtual_gateway_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.virtual_gateway_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualGatewayList:
    import aws_sdk_app_mesh.types.virtual_gateway_ref

    out: VirtualGatewayList = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.virtual_gateway_ref.deserialize_json(item))
    return out
