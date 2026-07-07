"""Generated from Smithy shape ``com.amazonaws.ivschat#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivschat.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.error_message
    import aws_sdk_ivschat.types.limit
    import aws_sdk_ivschat.types.resource_id
    import aws_sdk_ivschat.types.resource_type


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_ivschat.types.error_message.ErrorMessage"
    resource_id: "aws_sdk_ivschat.types.resource_id.ResourceId"
    """<p/>"""
    resource_type: "aws_sdk_ivschat.types.resource_type.ResourceType"
    """<p/>"""
    limit: "aws_sdk_ivschat.types.limit.Limit"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    out["limit"] = value.get("limit", 0)
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ThrottlingException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ThrottlingException_.resource_type required")
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivschat#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
