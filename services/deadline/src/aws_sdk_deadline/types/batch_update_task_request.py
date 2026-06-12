"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_task_items
    import aws_sdk_deadline.types.client_token


class BatchUpdateTaskRequest(TypedDict):
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    tasks: "aws_sdk_deadline.types.batch_update_task_items.BatchUpdateTaskItems"
    """<p>The list of tasks to update. You can specify up to 100 tasks per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_update_task_items

    out["tasks"] = aws_sdk_deadline.types.batch_update_task_items.serialize_json(
        value["tasks"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskRequest:
    out: BatchUpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_deadline.types.batch_update_task_items

        out["tasks"] = aws_sdk_deadline.types.batch_update_task_items.deserialize_json(
            data["tasks"]
        )
    else:
        raise DeserializationError("BatchUpdateTaskRequest.tasks required")
    return out
