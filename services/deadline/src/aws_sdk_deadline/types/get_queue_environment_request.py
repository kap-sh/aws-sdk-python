"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.queue_environment_id
    import aws_sdk_deadline.types.queue_id


class GetQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the queue environment.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue environment.</p>"""
    queue_environment_id: (
        "aws_sdk_deadline.types.queue_environment_id.QueueEnvironmentId"
    )
    """<p>The queue environment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueEnvironmentRequest:
    out: GetQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
