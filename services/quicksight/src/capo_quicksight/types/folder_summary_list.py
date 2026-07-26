"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.folder_summary

FolderSummaryList: TypeAlias = list[
    "capo_quicksight.types.folder_summary.FolderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderSummaryList) -> list:
    import capo_quicksight.types.folder_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.folder_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderSummaryList:
    import capo_quicksight.types.folder_summary

    out: FolderSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.folder_summary.deserialize_json(item))
    return out
