"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_summary

FlowSummaryList: TypeAlias = list["aws_sdk_quicksight.types.flow_summary.FlowSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowSummaryList) -> list:
    import aws_sdk_quicksight.types.flow_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.flow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowSummaryList:
    import aws_sdk_quicksight.types.flow_summary

    out: FlowSummaryList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.flow_summary.deserialize_json(item))
    return out
