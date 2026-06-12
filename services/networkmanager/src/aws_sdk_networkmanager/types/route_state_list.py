"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.route_state

RouteStateList: TypeAlias = list["aws_sdk_networkmanager.types.route_state.RouteState"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteStateList) -> list:
    import aws_sdk_networkmanager.types.route_state

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.route_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteStateList:
    import aws_sdk_networkmanager.types.route_state

    out: RouteStateList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.route_state.deserialize_json(item))
    return out
