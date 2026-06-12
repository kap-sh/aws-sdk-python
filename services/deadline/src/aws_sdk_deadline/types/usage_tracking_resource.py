"""Generated from Smithy shape ``com.amazonaws.deadline#UsageTrackingResource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.queue_id


class _UsageTrackingResource_queueId(TypedDict):
    queueId: "aws_sdk_deadline.types.queue_id.QueueId"


UsageTrackingResource: TypeAlias = _UsageTrackingResource_queueId


# --- restJson1 ser/de ---
def serialize_json(value: UsageTrackingResource) -> dict:
    if "queueId" in value:
        return {"queueId": value["queueId"]}
    else:
        raise SerializationError("UsageTrackingResource: no variant present")


def deserialize_json(data: dict) -> UsageTrackingResource:
    if "queueId" in data:
        return {"queueId": data["queueId"]}
    else:
        raise DeserializationError("UsageTrackingResource: no recognized variant key")
