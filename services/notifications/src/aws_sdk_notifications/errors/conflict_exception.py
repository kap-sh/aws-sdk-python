"""Generated from Smithy shape ``com.amazonaws.notifications#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_notifications.errors import DeserializationError
from aws_sdk_notifications.errors import ServiceError
if TYPE_CHECKING:
    import aws_sdk_notifications.types.error_message
    import aws_sdk_notifications.types.resource_id

class ConflictException_(TypedDict):
    message: "aws_sdk_notifications.types.error_message.ErrorMessage"
    resource_id: "aws_sdk_notifications.types.resource_id.ResourceId"
    """<p>The resource ID that prompted the conflict error.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notifications#ConflictException``."""
    code: str | None = 'ConflictException'

    def __init__(self, data: ConflictException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='ConflictException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))