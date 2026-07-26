"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_id


class BatchGetSessionIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the session.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the session.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID of the session.</p>"""
    session_id: "capo_deadline.types.session_id.SessionId"
    """<p>The session ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> BatchGetSessionIdentifier:
    out: BatchGetSessionIdentifier = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetSessionIdentifier.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetSessionIdentifier.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetSessionIdentifier.job_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("BatchGetSessionIdentifier.session_id required")
    return out
