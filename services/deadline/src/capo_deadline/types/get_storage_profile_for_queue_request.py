"""Generated from Smithy shape ``com.amazonaws.deadline#GetStorageProfileForQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.storage_profile_id


class GetStorageProfileForQueueRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the queue in storage profile.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID the queue in the storage profile.</p>"""
    storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID for the storage profile in the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageProfileForQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStorageProfileForQueueRequest:
    out: GetStorageProfileForQueueRequest = {}  # type: ignore[typeddict-item]
    return out
