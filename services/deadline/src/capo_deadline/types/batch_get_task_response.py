"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_task_errors
    import capo_deadline.types.batch_get_task_items


class BatchGetTaskResponse(TypedDict, closed=True):
    tasks: "capo_deadline.types.batch_get_task_items.BatchGetTaskItems"
    """<p>A list of tasks that were successfully retrieved.</p>"""
    errors: "capo_deadline.types.batch_get_task_errors.BatchGetTaskErrors"
    """<p>A list of errors for tasks that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_task_items

    out["tasks"] = capo_deadline.types.batch_get_task_items.serialize_json(
        value["tasks"]
    )
    import capo_deadline.types.batch_get_task_errors

    out["errors"] = capo_deadline.types.batch_get_task_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetTaskResponse:
    out: BatchGetTaskResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import capo_deadline.types.batch_get_task_items

        out["tasks"] = capo_deadline.types.batch_get_task_items.deserialize_json(
            data["tasks"]
        )
    else:
        raise DeserializationError("BatchGetTaskResponse.tasks required")
    if "errors" in data:
        import capo_deadline.types.batch_get_task_errors

        out["errors"] = capo_deadline.types.batch_get_task_errors.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchGetTaskResponse.errors required")
    return out
