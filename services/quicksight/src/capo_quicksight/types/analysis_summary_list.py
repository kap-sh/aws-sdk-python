"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_summary

AnalysisSummaryList: TypeAlias = list[
    "capo_quicksight.types.analysis_summary.AnalysisSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSummaryList) -> list:
    import capo_quicksight.types.analysis_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.analysis_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisSummaryList:
    import capo_quicksight.types.analysis_summary

    out: AnalysisSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.analysis_summary.deserialize_json(item))
    return out
