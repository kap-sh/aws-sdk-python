"""Generated from Smithy shape ``com.amazonaws.deadline#GetStorageProfileForQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.storage_profile_id


class GetStorageProfileForQueueRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the queue in storage profile.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID the queue in the storage profile.</p>"""
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID for the storage profile in the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageProfileForQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStorageProfileForQueueRequest:
    out: GetStorageProfileForQueueRequest = {}  # type: ignore[typeddict-item]
    return out
