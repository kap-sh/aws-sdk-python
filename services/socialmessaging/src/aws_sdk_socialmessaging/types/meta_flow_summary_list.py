"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_summary

MetaFlowSummaryList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.meta_flow_summary.MetaFlowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowSummaryList) -> list:
    import aws_sdk_socialmessaging.types.meta_flow_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_socialmessaging.types.meta_flow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetaFlowSummaryList:
    import aws_sdk_socialmessaging.types.meta_flow_summary

    out: MetaFlowSummaryList = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.meta_flow_summary.deserialize_json(item)
        )
    return out
