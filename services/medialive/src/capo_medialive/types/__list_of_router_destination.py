"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRouterDestination``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.router_destination

__listOfRouterDestination: TypeAlias = list[
    "capo_medialive.types.router_destination.RouterDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouterDestination) -> list:
    import capo_medialive.types.router_destination

    out: list = []
    for item in value:
        out.append(capo_medialive.types.router_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRouterDestination:
    import capo_medialive.types.router_destination

    out: __listOfRouterDestination = []
    for item in data:
        out.append(capo_medialive.types.router_destination.deserialize_json(item))
    return out
