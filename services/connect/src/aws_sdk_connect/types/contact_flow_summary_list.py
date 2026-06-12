"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_summary

ContactFlowSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_summary.ContactFlowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSummaryList) -> list:
    import aws_sdk_connect.types.contact_flow_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_flow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowSummaryList:
    import aws_sdk_connect.types.contact_flow_summary

    out: ContactFlowSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_flow_summary.deserialize_json(item))
    return out
