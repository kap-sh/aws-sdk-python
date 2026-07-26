"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_summary

MetaFlowSummaryList: TypeAlias = list[
    "capo_socialmessaging.types.meta_flow_summary.MetaFlowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowSummaryList) -> list:
    import capo_socialmessaging.types.meta_flow_summary

    out: list = []
    for item in value:
        out.append(capo_socialmessaging.types.meta_flow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetaFlowSummaryList:
    import capo_socialmessaging.types.meta_flow_summary

    out: MetaFlowSummaryList = []
    for item in data:
        out.append(capo_socialmessaging.types.meta_flow_summary.deserialize_json(item))
    return out
