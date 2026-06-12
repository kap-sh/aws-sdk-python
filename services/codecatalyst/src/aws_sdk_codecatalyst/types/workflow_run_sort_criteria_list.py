"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowRunSortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.workflow_run_sort_criteria

WorkflowRunSortCriteriaList: TypeAlias = list[
    "aws_sdk_codecatalyst.types.workflow_run_sort_criteria.WorkflowRunSortCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunSortCriteriaList) -> list:
    import aws_sdk_codecatalyst.types.workflow_run_sort_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecatalyst.types.workflow_run_sort_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowRunSortCriteriaList:
    import aws_sdk_codecatalyst.types.workflow_run_sort_criteria

    out: WorkflowRunSortCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_codecatalyst.types.workflow_run_sort_criteria.deserialize_json(item)
        )
    return out
