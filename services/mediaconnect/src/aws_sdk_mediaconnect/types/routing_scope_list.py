"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RoutingScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.routing_scope

RoutingScopeList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingScopeList) -> list:
    import aws_sdk_mediaconnect.types.routing_scope

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.routing_scope.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutingScopeList:
    import aws_sdk_mediaconnect.types.routing_scope

    out: RoutingScopeList = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.routing_scope.deserialize_json(item))
    return out
