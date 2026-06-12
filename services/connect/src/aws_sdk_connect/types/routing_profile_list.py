"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile

RoutingProfileList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile.RoutingProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileList) -> list:
    import aws_sdk_connect.types.routing_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.routing_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutingProfileList:
    import aws_sdk_connect.types.routing_profile

    out: RoutingProfileList = []
    for item in data:
        out.append(aws_sdk_connect.types.routing_profile.deserialize_json(item))
    return out
