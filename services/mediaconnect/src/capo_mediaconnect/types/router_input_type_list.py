"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_type

RouterInputTypeList: TypeAlias = list[
    "capo_mediaconnect.types.router_input_type.RouterInputType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTypeList) -> list:
    import capo_mediaconnect.types.router_input_type

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_input_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterInputTypeList:
    import capo_mediaconnect.types.router_input_type

    out: RouterInputTypeList = []
    for item in data:
        out.append(capo_mediaconnect.types.router_input_type.deserialize_json(item))
    return out
