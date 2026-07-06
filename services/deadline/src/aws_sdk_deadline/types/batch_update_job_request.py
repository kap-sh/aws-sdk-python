"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_job_items
    import aws_sdk_deadline.types.client_token


class BatchUpdateJobRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    jobs: "aws_sdk_deadline.types.batch_update_job_items.BatchUpdateJobItems"
    """<p>The list of jobs to update. You can specify up to 100 jobs per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_update_job_items

    out["jobs"] = aws_sdk_deadline.types.batch_update_job_items.serialize_json(
        value["jobs"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateJobRequest:
    out: BatchUpdateJobRequest = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_deadline.types.batch_update_job_items

        out["jobs"] = aws_sdk_deadline.types.batch_update_job_items.deserialize_json(
            data["jobs"]
        )
    else:
        raise DeserializationError("BatchUpdateJobRequest.jobs required")
    return out
