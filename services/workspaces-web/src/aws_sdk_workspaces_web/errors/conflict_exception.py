"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.exception_message
    import aws_sdk_workspaces_web.types.resource_id
    import aws_sdk_workspaces_web.types.resource_type


class ConflictException_(TypedDict):
    message: NotRequired[
        "aws_sdk_workspaces_web.types.exception_message.ExceptionMessage"
    ]
    resource_id: NotRequired["aws_sdk_workspaces_web.types.resource_id.ResourceId"]
    """<p>Identifier of the resource affected.</p>"""
    resource_type: NotRequired[
        "aws_sdk_workspaces_web.types.resource_type.ResourceType"
    ]
    """<p>Type of the resource affected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesweb#ConflictException``."""

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
