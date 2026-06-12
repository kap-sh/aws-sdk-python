"""Generated from Smithy shape ``com.amazonaws.batch#DeleteJobQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeleteJobQueueRequest(TypedDict):
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the queue to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobQueueRequest) -> dict:
    out: dict = {}
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    return out


def deserialize_json(data: dict) -> DeleteJobQueueRequest:
    out: DeleteJobQueueRequest = {}  # type: ignore[typeddict-item]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    return out
