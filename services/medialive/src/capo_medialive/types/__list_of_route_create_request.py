"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRouteCreateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.route_create_request

__listOfRouteCreateRequest: TypeAlias = list[
    "capo_medialive.types.route_create_request.RouteCreateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouteCreateRequest) -> list:
    import capo_medialive.types.route_create_request

    out: list = []
    for item in value:
        out.append(capo_medialive.types.route_create_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRouteCreateRequest:
    import capo_medialive.types.route_create_request

    out: __listOfRouteCreateRequest = []
    for item in data:
        out.append(capo_medialive.types.route_create_request.deserialize_json(item))
    return out
