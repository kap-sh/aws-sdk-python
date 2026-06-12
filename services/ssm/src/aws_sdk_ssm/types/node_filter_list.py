"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.node_filter

NodeFilterList: TypeAlias = list["aws_sdk_ssm.types.node_filter.NodeFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeFilterList) -> list:
    import aws_sdk_ssm.types.node_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.node_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeFilterList:
    import aws_sdk_ssm.types.node_filter

    out: NodeFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.node_filter.deserialize_aws_json_1_1(item))
    return out
