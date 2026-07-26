"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_summary

DataSetSummaryList: TypeAlias = list[
    "capo_quicksight.types.data_set_summary.DataSetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSummaryList) -> list:
    import capo_quicksight.types.data_set_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_set_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetSummaryList:
    import capo_quicksight.types.data_set_summary

    out: DataSetSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.data_set_summary.deserialize_json(item))
    return out
