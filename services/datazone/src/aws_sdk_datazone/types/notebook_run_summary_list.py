"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notebook_run_summary

NotebookRunSummaryList: TypeAlias = list[
    "aws_sdk_datazone.types.notebook_run_summary.NotebookRunSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookRunSummaryList) -> list:
    import aws_sdk_datazone.types.notebook_run_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.notebook_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotebookRunSummaryList:
    import aws_sdk_datazone.types.notebook_run_summary

    out: NotebookRunSummaryList = []
    for item in data:
        out.append(aws_sdk_datazone.types.notebook_run_summary.deserialize_json(item))
    return out
