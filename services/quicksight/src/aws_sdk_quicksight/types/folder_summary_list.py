"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.folder_summary

FolderSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.folder_summary.FolderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderSummaryList) -> list:
    import aws_sdk_quicksight.types.folder_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.folder_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderSummaryList:
    import aws_sdk_quicksight.types.folder_summary

    out: FolderSummaryList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.folder_summary.deserialize_json(item))
    return out
