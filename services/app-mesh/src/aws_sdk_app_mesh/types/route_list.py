"""Generated from Smithy shape ``com.amazonaws.appmesh#RouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.route_ref

RouteList: TypeAlias = list["aws_sdk_app_mesh.types.route_ref.RouteRef"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteList) -> list:
    import aws_sdk_app_mesh.types.route_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.route_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteList:
    import aws_sdk_app_mesh.types.route_ref

    out: RouteList = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.route_ref.deserialize_json(item))
    return out
