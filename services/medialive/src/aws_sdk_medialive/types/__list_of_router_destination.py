"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRouterDestination``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.router_destination

__listOfRouterDestination: TypeAlias = list[
    "aws_sdk_medialive.types.router_destination.RouterDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouterDestination) -> list:
    import aws_sdk_medialive.types.router_destination

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.router_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRouterDestination:
    import aws_sdk_medialive.types.router_destination

    out: __listOfRouterDestination = []
    for item in data:
        out.append(aws_sdk_medialive.types.router_destination.deserialize_json(item))
    return out
