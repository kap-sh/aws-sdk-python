"""Generated from Smithy shape ``com.amazonaws.appmesh#RouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.route_ref

RouteList: TypeAlias = list["capo_app_mesh.types.route_ref.RouteRef"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteList) -> list:
    import capo_app_mesh.types.route_ref

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.route_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteList:
    import capo_app_mesh.types.route_ref

    out: RouteList = []
    for item in data:
        out.append(capo_app_mesh.types.route_ref.deserialize_json(item))
    return out
