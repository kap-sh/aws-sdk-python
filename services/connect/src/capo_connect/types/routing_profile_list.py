"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.routing_profile

RoutingProfileList: TypeAlias = list[
    "capo_connect.types.routing_profile.RoutingProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileList) -> list:
    import capo_connect.types.routing_profile

    out: list = []
    for item in value:
        out.append(capo_connect.types.routing_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutingProfileList:
    import capo_connect.types.routing_profile

    out: RoutingProfileList = []
    for item in data:
        out.append(capo_connect.types.routing_profile.deserialize_json(item))
    return out
