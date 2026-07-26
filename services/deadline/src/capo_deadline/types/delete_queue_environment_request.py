"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_environment_id
    import capo_deadline.types.queue_id


class DeleteQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm from which to remove the queue environment.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the queue environment to delete.</p>"""
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """<p>The queue environment ID of the queue environment to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueEnvironmentRequest:
    out: DeleteQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
