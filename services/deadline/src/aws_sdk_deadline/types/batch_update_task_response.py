"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_task_errors


class BatchUpdateTaskResponse(TypedDict):
    errors: "aws_sdk_deadline.types.batch_update_task_errors.BatchUpdateTaskErrors"
    """<p>A list of errors for tasks that could not be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_update_task_errors

    out["errors"] = aws_sdk_deadline.types.batch_update_task_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskResponse:
    out: BatchUpdateTaskResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_deadline.types.batch_update_task_errors

        out["errors"] = (
            aws_sdk_deadline.types.batch_update_task_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateTaskResponse.errors required")
    return out
