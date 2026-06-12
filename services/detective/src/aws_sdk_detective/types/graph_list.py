"""Generated from Smithy shape ``com.amazonaws.detective#GraphList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph

GraphList: TypeAlias = list["aws_sdk_detective.types.graph.Graph"]


# --- restJson1 ser/de ---
def serialize_json(value: GraphList) -> list:
    import aws_sdk_detective.types.graph

    out: list = []
    for item in value:
        out.append(aws_sdk_detective.types.graph.serialize_json(item))
    return out


def deserialize_json(data: list) -> GraphList:
    import aws_sdk_detective.types.graph

    out: GraphList = []
    for item in data:
        out.append(aws_sdk_detective.types.graph.deserialize_json(item))
    return out
