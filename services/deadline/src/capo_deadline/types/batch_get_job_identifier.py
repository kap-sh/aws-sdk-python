"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id


class BatchGetJobIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the job.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the job.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> BatchGetJobIdentifier:
    out: BatchGetJobIdentifier = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetJobIdentifier.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetJobIdentifier.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetJobIdentifier.job_id required")
    return out
