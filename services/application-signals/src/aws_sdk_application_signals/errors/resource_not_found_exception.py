"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.fault_description
    import aws_sdk_application_signals.types.resource_id
    import aws_sdk_application_signals.types.resource_type


class ResourceNotFoundException_(TypedDict):
    resource_type: "aws_sdk_application_signals.types.resource_type.ResourceType"
    """<p>The resource type is not valid.</p>"""
    resource_id: "aws_sdk_application_signals.types.resource_id.ResourceId"
    """<p>Can't find the resource id.</p>"""
    message: "aws_sdk_application_signals.types.fault_description.FaultDescription"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    out["ResourceId"] = value["resource_id"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationsignals#ResourceNotFoundException``."""

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
