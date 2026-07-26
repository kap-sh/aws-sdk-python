"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunSessionActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.step_id
    import capo_deadline.types.task_id
    import capo_deadline.types.task_parameters


class TaskRunSessionActionDefinition(TypedDict, closed=True):
    task_id: NotRequired["capo_deadline.types.task_id.TaskId"]
    """<p>The task ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    parameters: "capo_deadline.types.task_parameters.TaskParameters"
    """<p>The task parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunSessionActionDefinition) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    out["stepId"] = value["step_id"]
    import capo_deadline.types.task_parameters

    out["parameters"] = capo_deadline.types.task_parameters.serialize_json(
        value["parameters"]
    )
    return out


def deserialize_json(data: dict) -> TaskRunSessionActionDefinition:
    out: TaskRunSessionActionDefinition = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("TaskRunSessionActionDefinition.step_id required")
    if "parameters" in data:
        import capo_deadline.types.task_parameters

        out["parameters"] = capo_deadline.types.task_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError("TaskRunSessionActionDefinition.parameters required")
    return out
