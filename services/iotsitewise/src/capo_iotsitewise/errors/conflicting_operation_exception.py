"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConflictingOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message
from capo_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message
    import capo_iotsitewise.types.resource_arn
    import capo_iotsitewise.types.resource_id


class ConflictingOperationException_(TypedDict, closed=True):
    message: "capo_iotsitewise.types.error_message.ErrorMessage"
    resource_id: "capo_iotsitewise.types.resource_id.ResourceId"
    """<p>The ID of the resource that conflicts with this operation.</p>"""
    resource_arn: "capo_iotsitewise.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource that conflicts with this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictingOperationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ConflictingOperationException_:
    out: ConflictingOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictingOperationException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "ConflictingOperationException_.resource_id required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "ConflictingOperationException_.resource_arn required"
        )
    return out


class ConflictingOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#ConflictingOperationException``."""

    code: str | None = "ConflictingOperationException"

    def __init__(self, data: ConflictingOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictingOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictingOperationException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ConflictingOperationException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "conflictingOperationException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConflictingOperationException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConflictingOperationException_ = {}  # type: ignore[typeddict-item]
    return out
