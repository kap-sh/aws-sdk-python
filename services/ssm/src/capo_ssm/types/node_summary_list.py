"""Generated from Smithy shape ``com.amazonaws.ssm#NodeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.node_summary

NodeSummaryList: TypeAlias = list["capo_ssm.types.node_summary.NodeSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeSummaryList) -> list:
    import capo_ssm.types.node_summary

    out: list = []
    for item in value:
        out.append(capo_ssm.types.node_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeSummaryList:
    import capo_ssm.types.node_summary

    out: NodeSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.node_summary.deserialize_aws_json_1_1(item))
    return out
