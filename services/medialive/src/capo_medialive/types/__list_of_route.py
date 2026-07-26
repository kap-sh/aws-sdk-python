"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRoute``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.route

__listOfRoute: TypeAlias = list["capo_medialive.types.route.Route"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoute) -> list:
    import capo_medialive.types.route

    out: list = []
    for item in value:
        out.append(capo_medialive.types.route.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRoute:
    import capo_medialive.types.route

    out: __listOfRoute = []
    for item in data:
        out.append(capo_medialive.types.route.deserialize_json(item))
    return out
