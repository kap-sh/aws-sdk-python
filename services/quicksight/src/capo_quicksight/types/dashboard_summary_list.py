"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_summary

DashboardSummaryList: TypeAlias = list[
    "capo_quicksight.types.dashboard_summary.DashboardSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSummaryList) -> list:
    import capo_quicksight.types.dashboard_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dashboard_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashboardSummaryList:
    import capo_quicksight.types.dashboard_summary

    out: DashboardSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.dashboard_summary.deserialize_json(item))
    return out
