"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.notebook_run_summary

NotebookRunSummaryList: TypeAlias = list[
    "capo_datazone.types.notebook_run_summary.NotebookRunSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookRunSummaryList) -> list:
    import capo_datazone.types.notebook_run_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.notebook_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotebookRunSummaryList:
    import capo_datazone.types.notebook_run_summary

    out: NotebookRunSummaryList = []
    for item in data:
        out.append(capo_datazone.types.notebook_run_summary.deserialize_json(item))
    return out
