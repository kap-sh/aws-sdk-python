"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_action_id


class BatchGetSessionActionIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the session action.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the session action.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID of the session action.</p>"""
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["sessionActionId"] = value["session_action_id"]
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionIdentifier:
    out: BatchGetSessionActionIdentifier = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetSessionActionIdentifier.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetSessionActionIdentifier.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetSessionActionIdentifier.job_id required")
    if "sessionActionId" in data:
        out["session_action_id"] = data["sessionActionId"]
    else:
        raise DeserializationError(
            "BatchGetSessionActionIdentifier.session_action_id required"
        )
    return out
