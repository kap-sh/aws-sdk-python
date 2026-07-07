"""Generated from Smithy shape ``com.amazonaws.transfer#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.message
    import aws_sdk_transfer.types.resource
    import aws_sdk_transfer.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_transfer.types.message.Message"
    resource: "aws_sdk_transfer.types.resource.Resource"
    resource_type: "aws_sdk_transfer.types.resource_type.ResourceType"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["Resource"] = value["resource"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "Resource" in data:
        out["resource"] = data["Resource"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transfer#ResourceNotFoundException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
