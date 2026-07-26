"""Generated from Smithy shape ``com.amazonaws.eks#CapabilitySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.capability_summary

CapabilitySummaryList: TypeAlias = list[
    "capo_eks.types.capability_summary.CapabilitySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilitySummaryList) -> list:
    import capo_eks.types.capability_summary

    out: list = []
    for item in value:
        out.append(capo_eks.types.capability_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapabilitySummaryList:
    import capo_eks.types.capability_summary

    out: CapabilitySummaryList = []
    for item in data:
        out.append(capo_eks.types.capability_summary.deserialize_json(item))
    return out
