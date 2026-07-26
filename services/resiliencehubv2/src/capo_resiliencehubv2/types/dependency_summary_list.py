"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dependency_summary

DependencySummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.dependency_summary.DependencySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencySummaryList) -> list:
    import capo_resiliencehubv2.types.dependency_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.dependency_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DependencySummaryList:
    import capo_resiliencehubv2.types.dependency_summary

    out: DependencySummaryList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.dependency_summary.deserialize_json(item))
    return out
