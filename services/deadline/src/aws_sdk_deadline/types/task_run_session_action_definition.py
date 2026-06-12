"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunSessionActionDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.task_id
    import aws_sdk_deadline.types.task_parameters


class TaskRunSessionActionDefinition(TypedDict):
    task_id: NotRequired["aws_sdk_deadline.types.task_id.TaskId"]
    """<p>The task ID.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    parameters: "aws_sdk_deadline.types.task_parameters.TaskParameters"
    """<p>The task parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunSessionActionDefinition) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    out["stepId"] = value["step_id"]
    import aws_sdk_deadline.types.task_parameters

    out["parameters"] = aws_sdk_deadline.types.task_parameters.serialize_json(
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
        import aws_sdk_deadline.types.task_parameters

        out["parameters"] = aws_sdk_deadline.types.task_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError("TaskRunSessionActionDefinition.parameters required")
    return out
