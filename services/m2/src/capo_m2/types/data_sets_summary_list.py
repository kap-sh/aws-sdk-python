"""Generated from Smithy shape ``com.amazonaws.m2#DataSetsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.data_set_summary

DataSetsSummaryList: TypeAlias = list["capo_m2.types.data_set_summary.DataSetSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetsSummaryList) -> list:
    import capo_m2.types.data_set_summary

    out: list = []
    for item in value:
        out.append(capo_m2.types.data_set_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetsSummaryList:
    import capo_m2.types.data_set_summary

    out: DataSetsSummaryList = []
    for item in data:
        out.append(capo_m2.types.data_set_summary.deserialize_json(item))
    return out
