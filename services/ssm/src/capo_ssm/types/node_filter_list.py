"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.node_filter

NodeFilterList: TypeAlias = list["capo_ssm.types.node_filter.NodeFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeFilterList) -> list:
    import capo_ssm.types.node_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.node_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeFilterList:
    import capo_ssm.types.node_filter

    out: NodeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.node_filter.deserialize_aws_json_1_1(item))
    return out
