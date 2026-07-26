"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowRunStatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.workflow_run_status_reason

WorkflowRunStatusReasons: TypeAlias = list[
    "capo_codecatalyst.types.workflow_run_status_reason.WorkflowRunStatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunStatusReasons) -> list:
    import capo_codecatalyst.types.workflow_run_status_reason

    out: list = []
    for item in value:
        out.append(
            capo_codecatalyst.types.workflow_run_status_reason.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowRunStatusReasons:
    import capo_codecatalyst.types.workflow_run_status_reason

    out: WorkflowRunStatusReasons = []
    for item in data:
        out.append(
            capo_codecatalyst.types.workflow_run_status_reason.deserialize_json(item)
        )
    return out
