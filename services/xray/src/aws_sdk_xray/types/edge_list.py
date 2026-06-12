"""Generated from Smithy shape ``com.amazonaws.xray#EdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.edge

EdgeList: TypeAlias = list["aws_sdk_xray.types.edge.Edge"]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeList) -> list:
    import aws_sdk_xray.types.edge

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.edge.serialize_json(item))
    return out


def deserialize_json(data: list) -> EdgeList:
    import aws_sdk_xray.types.edge

    out: EdgeList = []
    for item in data:
        out.append(aws_sdk_xray.types.edge.deserialize_json(item))
    return out
