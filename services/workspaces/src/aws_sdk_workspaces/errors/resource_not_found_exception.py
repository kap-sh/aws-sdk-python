"""Generated from Smithy shape ``com.amazonaws.workspaces#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_message
    import aws_sdk_workspaces.types.non_empty_string


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]
    """<p>The resource could not be found.</p>"""
    resource_id: NotRequired["aws_sdk_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the resource that could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#ResourceNotFoundException``."""

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
