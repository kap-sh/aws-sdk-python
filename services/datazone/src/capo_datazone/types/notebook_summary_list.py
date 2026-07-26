"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.notebook_summary

NotebookSummaryList: TypeAlias = list[
    "capo_datazone.types.notebook_summary.NotebookSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookSummaryList) -> list:
    import capo_datazone.types.notebook_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.notebook_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotebookSummaryList:
    import capo_datazone.types.notebook_summary

    out: NotebookSummaryList = []
    for item in data:
        out.append(capo_datazone.types.notebook_summary.deserialize_json(item))
    return out
