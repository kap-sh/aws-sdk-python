"""Generated from Smithy shape ``com.amazonaws.workspaces#ResourceInUseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_message
    import aws_sdk_workspaces.types.non_empty_string


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]
    resource_id: NotRequired["aws_sdk_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the resource that is in use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(self, data: ResourceInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceInUseException":
        return cls(deserialize_aws_json_1_1(data))
