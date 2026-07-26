"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input

RouterInputList: TypeAlias = list["capo_mediaconnect.types.router_input.RouterInput"]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputList) -> list:
    import capo_mediaconnect.types.router_input

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterInputList:
    import capo_mediaconnect.types.router_input

    out: RouterInputList = []
    for item in data:
        out.append(capo_mediaconnect.types.router_input.deserialize_json(item))
    return out
