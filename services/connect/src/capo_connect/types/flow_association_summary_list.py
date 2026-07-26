"""Generated from Smithy shape ``com.amazonaws.connect#FlowAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.flow_association_summary

FlowAssociationSummaryList: TypeAlias = list[
    "capo_connect.types.flow_association_summary.FlowAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowAssociationSummaryList) -> list:
    import capo_connect.types.flow_association_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.flow_association_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowAssociationSummaryList:
    import capo_connect.types.flow_association_summary

    out: FlowAssociationSummaryList = []
    for item in data:
        out.append(capo_connect.types.flow_association_summary.deserialize_json(item))
    return out
