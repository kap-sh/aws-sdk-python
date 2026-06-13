"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.exception_resource_type
    import aws_sdk_quicksight.types.string


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    resource_type: NotRequired[
        "aws_sdk_quicksight.types.exception_resource_type.ExceptionResourceType"
    ]
    """<p>The resource type for this request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        import aws_sdk_quicksight.types.exception_resource_type

        out["ResourceType"] = (
            aws_sdk_quicksight.types.exception_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        import aws_sdk_quicksight.types.exception_resource_type

        out["resource_type"] = (
            aws_sdk_quicksight.types.exception_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#ResourceNotFoundException``."""

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
