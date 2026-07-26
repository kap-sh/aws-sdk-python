"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_summary

WorkflowSummaryList: TypeAlias = list[
    "capo_imagebuilder.types.workflow_summary.WorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSummaryList) -> list:
    import capo_imagebuilder.types.workflow_summary

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.workflow_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowSummaryList:
    import capo_imagebuilder.types.workflow_summary

    out: WorkflowSummaryList = []
    for item in data:
        out.append(capo_imagebuilder.types.workflow_summary.deserialize_json(item))
    return out
