"""Generated from Smithy shape ``com.amazonaws.batch#GetJobQueueSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class GetJobQueueSnapshotRequest(TypedDict):
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job queue’s name or full queue Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobQueueSnapshotRequest) -> dict:
    out: dict = {}
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    return out


def deserialize_json(data: dict) -> GetJobQueueSnapshotRequest:
    out: GetJobQueueSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    return out
