"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowSortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.workflow_sort_criteria

WorkflowSortCriteriaList: TypeAlias = list[
    "capo_codecatalyst.types.workflow_sort_criteria.WorkflowSortCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSortCriteriaList) -> list:
    import capo_codecatalyst.types.workflow_sort_criteria

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.workflow_sort_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowSortCriteriaList:
    import capo_codecatalyst.types.workflow_sort_criteria

    out: WorkflowSortCriteriaList = []
    for item in data:
        out.append(
            capo_codecatalyst.types.workflow_sort_criteria.deserialize_json(item)
        )
    return out
