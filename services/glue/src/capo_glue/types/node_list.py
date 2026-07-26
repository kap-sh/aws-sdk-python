"""Generated from Smithy shape ``com.amazonaws.glue#NodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.node

NodeList: TypeAlias = list["capo_glue.types.node.Node"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeList) -> list:
    import capo_glue.types.node

    out: list = []
    for item in value:
        out.append(capo_glue.types.node.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeList:
    import capo_glue.types.node

    out: NodeList = []
    for item in data:
        out.append(capo_glue.types.node.deserialize_aws_json_1_1(item))
    return out
