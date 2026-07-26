"""Generated from Smithy shape ``com.amazonaws.connect#DataTableSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_summary

DataTableSummaryList: TypeAlias = list[
    "capo_connect.types.data_table_summary.DataTableSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableSummaryList) -> list:
    import capo_connect.types.data_table_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.data_table_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataTableSummaryList:
    import capo_connect.types.data_table_summary

    out: DataTableSummaryList = []
    for item in data:
        out.append(capo_connect.types.data_table_summary.deserialize_json(item))
    return out
