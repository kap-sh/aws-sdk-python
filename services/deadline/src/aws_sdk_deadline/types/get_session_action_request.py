"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.session_action_id


class GetSessionActionRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the session action.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the session action.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID for the session.</p>"""
    session_action_id: "aws_sdk_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionActionRequest:
    out: GetSessionActionRequest = {}  # type: ignore[typeddict-item]
    return out
