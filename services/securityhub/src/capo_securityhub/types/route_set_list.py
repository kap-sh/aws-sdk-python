"""Generated from Smithy shape ``com.amazonaws.securityhub#RouteSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.route_set_details

RouteSetList: TypeAlias = list[
    "capo_securityhub.types.route_set_details.RouteSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSetList) -> list:
    import capo_securityhub.types.route_set_details

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.route_set_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteSetList:
    import capo_securityhub.types.route_set_details

    out: RouteSetList = []
    for item in data:
        out.append(capo_securityhub.types.route_set_details.deserialize_json(item))
    return out
