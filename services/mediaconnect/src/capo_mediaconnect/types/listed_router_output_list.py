"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_router_output

ListedRouterOutputList: TypeAlias = list[
    "capo_mediaconnect.types.listed_router_output.ListedRouterOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterOutputList) -> list:
    import capo_mediaconnect.types.listed_router_output

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.listed_router_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListedRouterOutputList:
    import capo_mediaconnect.types.listed_router_output

    out: ListedRouterOutputList = []
    for item in data:
        out.append(capo_mediaconnect.types.listed_router_output.deserialize_json(item))
    return out
