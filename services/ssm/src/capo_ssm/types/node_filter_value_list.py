"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.node_filter_value

NodeFilterValueList: TypeAlias = list[
    "capo_ssm.types.node_filter_value.NodeFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NodeFilterValueList:
    return list(data)
