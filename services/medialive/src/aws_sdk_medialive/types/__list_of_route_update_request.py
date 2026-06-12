"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRouteUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.route_update_request

__listOfRouteUpdateRequest: TypeAlias = list[
    "aws_sdk_medialive.types.route_update_request.RouteUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouteUpdateRequest) -> list:
    import aws_sdk_medialive.types.route_update_request

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.route_update_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRouteUpdateRequest:
    import aws_sdk_medialive.types.route_update_request

    out: __listOfRouteUpdateRequest = []
    for item in data:
        out.append(aws_sdk_medialive.types.route_update_request.deserialize_json(item))
    return out
