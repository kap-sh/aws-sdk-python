"""Generated from Smithy shape ``com.amazonaws.finspacedata#DataViewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.data_view_summary

DataViewList: TypeAlias = list[
    "capo_finspace_data.types.data_view_summary.DataViewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataViewList) -> list:
    import capo_finspace_data.types.data_view_summary

    out: list = []
    for item in value:
        out.append(capo_finspace_data.types.data_view_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataViewList:
    import capo_finspace_data.types.data_view_summary

    out: DataViewList = []
    for item in data:
        out.append(capo_finspace_data.types.data_view_summary.deserialize_json(item))
    return out
