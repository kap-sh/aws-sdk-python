"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.compute_node_group_summary

ComputeNodeGroupList: TypeAlias = list[
    "capo_pcs.types.compute_node_group_summary.ComputeNodeGroupSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroupList) -> list:
    import capo_pcs.types.compute_node_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_pcs.types.compute_node_group_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ComputeNodeGroupList:
    import capo_pcs.types.compute_node_group_summary

    out: ComputeNodeGroupList = []
    for item in data:
        out.append(
            capo_pcs.types.compute_node_group_summary.deserialize_aws_json_1_0(item)
        )
    return out
