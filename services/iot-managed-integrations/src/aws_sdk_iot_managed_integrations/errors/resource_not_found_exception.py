"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_managed_integrations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.error_message
    import aws_sdk_iot_managed_integrations.types.error_resource_id
    import aws_sdk_iot_managed_integrations.types.error_resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_iot_managed_integrations.types.error_message.ErrorMessage"
    ]
    resource_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.error_resource_id.ErrorResourceId"
    ]
    """Id of the affected resource"""
    resource_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.error_resource_type.ErrorResourceType"
    ]
    """Type of the affected resource"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotmanagedintegrations#ResourceNotFoundException``."""

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
