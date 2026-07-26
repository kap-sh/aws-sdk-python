"""Generated from Smithy shape ``com.amazonaws.ivschat#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivschat.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ivschat.types.error_message
    import capo_ivschat.types.resource_id
    import capo_ivschat.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: "capo_ivschat.types.error_message.ErrorMessage"
    resource_id: "capo_ivschat.types.resource_id.ResourceId"
    """<p/>"""
    resource_type: "capo_ivschat.types.resource_type.ResourceType"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
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
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivschat#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
