"""Generated from Smithy shape ``com.amazonaws.xray#LinksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.graph_link

LinksList: TypeAlias = list["aws_sdk_xray.types.graph_link.GraphLink"]


# --- restJson1 ser/de ---
def serialize_json(value: LinksList) -> list:
    import aws_sdk_xray.types.graph_link

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.graph_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinksList:
    import aws_sdk_xray.types.graph_link

    out: LinksList = []
    for item in data:
        out.append(aws_sdk_xray.types.graph_link.deserialize_json(item))
    return out
