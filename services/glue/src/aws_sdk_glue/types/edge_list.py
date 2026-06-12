"""Generated from Smithy shape ``com.amazonaws.glue#EdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.edge

EdgeList: TypeAlias = list["aws_sdk_glue.types.edge.Edge"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeList) -> list:
    import aws_sdk_glue.types.edge

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.edge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeList:
    import aws_sdk_glue.types.edge

    out: EdgeList = []
    for item in data:
        out.append(aws_sdk_glue.types.edge.deserialize_aws_json_1_1(item))
    return out
