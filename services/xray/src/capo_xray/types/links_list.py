"""Generated from Smithy shape ``com.amazonaws.xray#LinksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.graph_link

LinksList: TypeAlias = list["capo_xray.types.graph_link.GraphLink"]


# --- restJson1 ser/de ---
def serialize_json(value: LinksList) -> list:
    import capo_xray.types.graph_link

    out: list = []
    for item in value:
        out.append(capo_xray.types.graph_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinksList:
    import capo_xray.types.graph_link

    out: LinksList = []
    for item in data:
        out.append(capo_xray.types.graph_link.deserialize_json(item))
    return out
