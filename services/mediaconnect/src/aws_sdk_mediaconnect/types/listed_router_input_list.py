"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_router_input

ListedRouterInputList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_router_input.ListedRouterInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterInputList) -> list:
    import aws_sdk_mediaconnect.types.listed_router_input

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.listed_router_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListedRouterInputList:
    import aws_sdk_mediaconnect.types.listed_router_input

    out: ListedRouterInputList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.listed_router_input.deserialize_json(item)
        )
    return out
