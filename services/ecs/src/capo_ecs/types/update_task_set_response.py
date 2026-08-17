"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.task_set


class UpdateTaskSetResponse(TypedDict, closed=True):
    task_set: NotRequired["capo_ecs.types.task_set.TaskSet"]
    """<p>Details about the task set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskSetResponse) -> dict:
    out: dict = {}
    if "task_set" in value:
        import capo_ecs.types.task_set

        out["taskSet"] = capo_ecs.types.task_set.serialize_aws_json_1_1(
            value["task_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskSetResponse:
    out: UpdateTaskSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskSet") is not None:
        import capo_ecs.types.task_set

        out["task_set"] = capo_ecs.types.task_set.deserialize_aws_json_1_1(
            data["taskSet"]
        )
    return out
