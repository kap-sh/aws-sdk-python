"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowRunSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.workflow_run_summary

WorkflowRunSummaries: TypeAlias = list[
    "capo_codecatalyst.types.workflow_run_summary.WorkflowRunSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunSummaries) -> list:
    import capo_codecatalyst.types.workflow_run_summary

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.workflow_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowRunSummaries:
    import capo_codecatalyst.types.workflow_run_summary

    out: WorkflowRunSummaries = []
    for item in data:
        out.append(capo_codecatalyst.types.workflow_run_summary.deserialize_json(item))
    return out
