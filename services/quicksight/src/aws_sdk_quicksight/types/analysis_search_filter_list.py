"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_search_filter

AnalysisSearchFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.analysis_search_filter.AnalysisSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSearchFilterList) -> list:
    import aws_sdk_quicksight.types.analysis_search_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.analysis_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisSearchFilterList:
    import aws_sdk_quicksight.types.analysis_search_filter

    out: AnalysisSearchFilterList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.analysis_search_filter.deserialize_json(item)
        )
    return out
