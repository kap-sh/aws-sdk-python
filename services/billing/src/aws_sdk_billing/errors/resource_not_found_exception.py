"""Generated from Smithy shape ``com.amazonaws.billing#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_billing.types.error_message
    import aws_sdk_billing.types.resource_id
    import aws_sdk_billing.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_billing.types.error_message.ErrorMessage"
    resource_id: "aws_sdk_billing.types.resource_id.ResourceId"
    """<p> Value is a list of resource IDs that were not found. </p>"""
    resource_type: "aws_sdk_billing.types.resource_type.ResourceType"
    """<p> Value is the type of resource that was not found. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billing#ResourceNotFoundException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data))
