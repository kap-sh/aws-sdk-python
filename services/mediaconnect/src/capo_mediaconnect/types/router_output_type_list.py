"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_type

RouterOutputTypeList: TypeAlias = list[
    "capo_mediaconnect.types.router_output_type.RouterOutputType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputTypeList) -> list:
    import capo_mediaconnect.types.router_output_type

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_output_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterOutputTypeList:
    import capo_mediaconnect.types.router_output_type

    out: RouterOutputTypeList = []
    for item in data:
        out.append(capo_mediaconnect.types.router_output_type.deserialize_json(item))
    return out
