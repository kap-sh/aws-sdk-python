"""Generated from Smithy shape ``com.amazonaws.iot#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2
    import aws_sdk_iot.types.resource_arn
    import aws_sdk_iot.types.resource_id


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""
    resource_id: NotRequired["aws_sdk_iot.types.resource_id.resourceId"]
    """<p>The ID of the resource that caused the exception.</p>"""
    resource_arn: NotRequired["aws_sdk_iot.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource that caused the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#ResourceAlreadyExistsException``."""

    code: str | None = "ResourceAlreadyExistsException"

    def __init__(self, data: ResourceAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceAlreadyExistsException":
        return cls(deserialize_json(data))
