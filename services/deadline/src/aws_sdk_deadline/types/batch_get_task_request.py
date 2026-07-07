"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_task_identifiers


class BatchGetTaskRequest(TypedDict, closed=True):
    identifiers: (
        "aws_sdk_deadline.types.batch_get_task_identifiers.BatchGetTaskIdentifiers"
    )
    """<p>The list of task identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_task_identifiers

    out["identifiers"] = (
        aws_sdk_deadline.types.batch_get_task_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetTaskRequest:
    out: BatchGetTaskRequest = {}  # type: ignore[typeddict-item]
    if "identifiers" in data:
        import aws_sdk_deadline.types.batch_get_task_identifiers

        out["identifiers"] = (
            aws_sdk_deadline.types.batch_get_task_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        raise DeserializationError("BatchGetTaskRequest.identifiers required")
    return out
