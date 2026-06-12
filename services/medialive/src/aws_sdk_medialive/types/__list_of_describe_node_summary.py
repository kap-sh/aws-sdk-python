"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeNodeSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.describe_node_summary

__listOfDescribeNodeSummary: TypeAlias = list[
    "aws_sdk_medialive.types.describe_node_summary.DescribeNodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeNodeSummary) -> list:
    import aws_sdk_medialive.types.describe_node_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.describe_node_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDescribeNodeSummary:
    import aws_sdk_medialive.types.describe_node_summary

    out: __listOfDescribeNodeSummary = []
    for item in data:
        out.append(aws_sdk_medialive.types.describe_node_summary.deserialize_json(item))
    return out
