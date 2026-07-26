"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_source_summary

DataSourceSummaryList: TypeAlias = list[
    "capo_quicksight.types.data_source_summary.DataSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummaryList) -> list:
    import capo_quicksight.types.data_source_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_source_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceSummaryList:
    import capo_quicksight.types.data_source_summary

    out: DataSourceSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.data_source_summary.deserialize_json(item))
    return out
