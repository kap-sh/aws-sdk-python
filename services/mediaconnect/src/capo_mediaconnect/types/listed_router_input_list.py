"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_router_input

ListedRouterInputList: TypeAlias = list[
    "capo_mediaconnect.types.listed_router_input.ListedRouterInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterInputList) -> list:
    import capo_mediaconnect.types.listed_router_input

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.listed_router_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListedRouterInputList:
    import capo_mediaconnect.types.listed_router_input

    out: ListedRouterInputList = []
    for item in data:
        out.append(capo_mediaconnect.types.listed_router_input.deserialize_json(item))
    return out
