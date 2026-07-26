"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_version_summary

DashboardVersionSummaryList: TypeAlias = list[
    "capo_quicksight.types.dashboard_version_summary.DashboardVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVersionSummaryList) -> list:
    import capo_quicksight.types.dashboard_version_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dashboard_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashboardVersionSummaryList:
    import capo_quicksight.types.dashboard_version_summary

    out: DashboardVersionSummaryList = []
    for item in data:
        out.append(
            capo_quicksight.types.dashboard_version_summary.deserialize_json(item)
        )
    return out
