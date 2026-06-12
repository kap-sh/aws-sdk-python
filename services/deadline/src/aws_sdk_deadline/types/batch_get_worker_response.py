"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_worker_errors
    import aws_sdk_deadline.types.batch_get_worker_items


class BatchGetWorkerResponse(TypedDict):
    workers: "aws_sdk_deadline.types.batch_get_worker_items.BatchGetWorkerItems"
    """<p>A list of workers that were successfully retrieved.</p>"""
    errors: "aws_sdk_deadline.types.batch_get_worker_errors.BatchGetWorkerErrors"
    """<p>A list of errors for workers that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_worker_items

    out["workers"] = aws_sdk_deadline.types.batch_get_worker_items.serialize_json(
        value["workers"]
    )
    import aws_sdk_deadline.types.batch_get_worker_errors

    out["errors"] = aws_sdk_deadline.types.batch_get_worker_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetWorkerResponse:
    out: BatchGetWorkerResponse = {}  # type: ignore[typeddict-item]
    if "workers" in data:
        import aws_sdk_deadline.types.batch_get_worker_items

        out["workers"] = aws_sdk_deadline.types.batch_get_worker_items.deserialize_json(
            data["workers"]
        )
    else:
        raise DeserializationError("BatchGetWorkerResponse.workers required")
    if "errors" in data:
        import aws_sdk_deadline.types.batch_get_worker_errors

        out["errors"] = aws_sdk_deadline.types.batch_get_worker_errors.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchGetWorkerResponse.errors required")
    return out
