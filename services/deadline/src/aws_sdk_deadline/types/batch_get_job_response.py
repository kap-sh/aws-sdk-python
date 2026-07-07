"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_job_errors
    import aws_sdk_deadline.types.batch_get_job_items


class BatchGetJobResponse(TypedDict, closed=True):
    jobs: "aws_sdk_deadline.types.batch_get_job_items.BatchGetJobItems"
    """<p>A list of jobs that were successfully retrieved.</p>"""
    errors: "aws_sdk_deadline.types.batch_get_job_errors.BatchGetJobErrors"
    """<p>A list of errors for jobs that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_job_items

    out["jobs"] = aws_sdk_deadline.types.batch_get_job_items.serialize_json(
        value["jobs"]
    )
    import aws_sdk_deadline.types.batch_get_job_errors

    out["errors"] = aws_sdk_deadline.types.batch_get_job_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobResponse:
    out: BatchGetJobResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_deadline.types.batch_get_job_items

        out["jobs"] = aws_sdk_deadline.types.batch_get_job_items.deserialize_json(
            data["jobs"]
        )
    else:
        raise DeserializationError("BatchGetJobResponse.jobs required")
    if "errors" in data:
        import aws_sdk_deadline.types.batch_get_job_errors

        out["errors"] = aws_sdk_deadline.types.batch_get_job_errors.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchGetJobResponse.errors required")
    return out
