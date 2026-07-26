"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output

RouterOutputList: TypeAlias = list["capo_mediaconnect.types.router_output.RouterOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputList) -> list:
    import capo_mediaconnect.types.router_output

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterOutputList:
    import capo_mediaconnect.types.router_output

    out: RouterOutputList = []
    for item in data:
        out.append(capo_mediaconnect.types.router_output.deserialize_json(item))
    return out
