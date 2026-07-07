"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.session_id
    import aws_sdk_deadline.types.session_lifecycle_target_status


class UpdateSessionRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update in the session.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID to update in the session.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID to update in the session.</p>"""
    session_id: "aws_sdk_deadline.types.session_id.SessionId"
    """<p>The session ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    target_lifecycle_status: "aws_sdk_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    """<p>The life cycle status to update in the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.session_lifecycle_target_status

    out["targetLifecycleStatus"] = (
        aws_sdk_deadline.types.session_lifecycle_target_status.serialize_json(
            value["target_lifecycle_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionRequest:
    out: UpdateSessionRequest = {}  # type: ignore[typeddict-item]
    if "targetLifecycleStatus" in data:
        import aws_sdk_deadline.types.session_lifecycle_target_status

        out["target_lifecycle_status"] = (
            aws_sdk_deadline.types.session_lifecycle_target_status.deserialize_json(
                data["targetLifecycleStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSessionRequest.target_lifecycle_status required"
        )
    return out
