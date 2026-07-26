"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.route_state

RouteStateList: TypeAlias = list["capo_networkmanager.types.route_state.RouteState"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteStateList) -> list:
    import capo_networkmanager.types.route_state

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.route_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteStateList:
    import capo_networkmanager.types.route_state

    out: RouteStateList = []
    for item in data:
        out.append(capo_networkmanager.types.route_state.deserialize_json(item))
    return out
