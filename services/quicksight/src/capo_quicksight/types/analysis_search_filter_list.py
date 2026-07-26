"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_search_filter

AnalysisSearchFilterList: TypeAlias = list[
    "capo_quicksight.types.analysis_search_filter.AnalysisSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSearchFilterList) -> list:
    import capo_quicksight.types.analysis_search_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.analysis_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisSearchFilterList:
    import capo_quicksight.types.analysis_search_filter

    out: AnalysisSearchFilterList = []
    for item in data:
        out.append(capo_quicksight.types.analysis_search_filter.deserialize_json(item))
    return out
