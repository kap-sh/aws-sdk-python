"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.exception_message
    import aws_sdk_ssm_incidents.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_ssm_incidents.types.exception_message.ExceptionMessage"
    resource_identifier: NotRequired["str"]
    """The identifier for the requested resource"""
    resource_type: NotRequired["aws_sdk_ssm_incidents.types.resource_type.ResourceType"]
    """The resource type"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ResourceNotFoundException``."""

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
