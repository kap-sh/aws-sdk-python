"""Generated from Smithy shape ``com.amazonaws.glue#EdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.edge

EdgeList: TypeAlias = list["capo_glue.types.edge.Edge"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeList) -> list:
    import capo_glue.types.edge

    out: list = []
    for item in value:
        out.append(capo_glue.types.edge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeList:
    import capo_glue.types.edge

    out: EdgeList = []
    for item in data:
        out.append(capo_glue.types.edge.deserialize_aws_json_1_1(item))
    return out
