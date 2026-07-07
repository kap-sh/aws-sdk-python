"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_thin_client.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.exception_message
    import aws_sdk_workspaces_thin_client.types.resource_id
    import aws_sdk_workspaces_thin_client.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_workspaces_thin_client.types.exception_message.ExceptionMessage"
    ]
    resource_id: NotRequired[
        "aws_sdk_workspaces_thin_client.types.resource_id.ResourceId"
    ]
    """<p>The ID of the resource associated with the request.</p>"""
    resource_type: NotRequired[
        "aws_sdk_workspaces_thin_client.types.resource_type.ResourceType"
    ]
    """<p>The type of the resource associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesthinclient#ResourceNotFoundException``."""

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
