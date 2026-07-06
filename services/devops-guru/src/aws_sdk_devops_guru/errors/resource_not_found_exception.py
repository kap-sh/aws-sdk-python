"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.error_message_string
    import aws_sdk_devops_guru.types.resource_id_string
    import aws_sdk_devops_guru.types.resource_id_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_devops_guru.types.error_message_string.ErrorMessageString"
    resource_id: "aws_sdk_devops_guru.types.resource_id_string.ResourceIdString"
    """<p> The ID of the Amazon Web Services resource that could not be found. </p>"""
    resource_type: "aws_sdk_devops_guru.types.resource_id_type.ResourceIdType"
    """<p> The type of the Amazon Web Services resource that could not be found. </p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.devopsguru#ResourceNotFoundException``."""

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
