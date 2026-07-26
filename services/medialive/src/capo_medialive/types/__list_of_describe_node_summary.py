"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDescribeNodeSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.describe_node_summary

__listOfDescribeNodeSummary: TypeAlias = list[
    "capo_medialive.types.describe_node_summary.DescribeNodeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDescribeNodeSummary) -> list:
    import capo_medialive.types.describe_node_summary

    out: list = []
    for item in value:
        out.append(capo_medialive.types.describe_node_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDescribeNodeSummary:
    import capo_medialive.types.describe_node_summary

    out: __listOfDescribeNodeSummary = []
    for item in data:
        out.append(capo_medialive.types.describe_node_summary.deserialize_json(item))
    return out
