"""Generated from Smithy shape ``com.amazonaws.billingconductor#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_billingconductor.types.string.String"
    resource_id: "aws_sdk_billingconductor.types.string.String"
    """<p>Resource identifier that was not found. </p>"""
    resource_type: "aws_sdk_billingconductor.types.string.String"
    """<p>Resource type that was not found. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billingconductor#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
