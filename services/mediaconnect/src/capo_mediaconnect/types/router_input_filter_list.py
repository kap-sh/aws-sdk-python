"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_filter

RouterInputFilterList: TypeAlias = list[
    "capo_mediaconnect.types.router_input_filter.RouterInputFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputFilterList) -> list:
    import capo_mediaconnect.types.router_input_filter

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_input_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterInputFilterList:
    import capo_mediaconnect.types.router_input_filter

    out: RouterInputFilterList = []
    for item in data:
        out.append(capo_mediaconnect.types.router_input_filter.deserialize_json(item))
    return out
