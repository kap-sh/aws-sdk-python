"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.route_type

RouteTypeList: TypeAlias = list["capo_networkmanager.types.route_type.RouteType"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTypeList) -> list:
    import capo_networkmanager.types.route_type

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.route_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTypeList:
    import capo_networkmanager.types.route_type

    out: RouteTypeList = []
    for item in data:
        out.append(capo_networkmanager.types.route_type.deserialize_json(item))
    return out
