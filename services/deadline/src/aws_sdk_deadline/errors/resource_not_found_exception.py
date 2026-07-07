"""Generated from Smithy shape ``com.amazonaws.deadline#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.exception_context
    import aws_sdk_deadline.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_deadline.types.string.String"
    resource_id: "aws_sdk_deadline.types.string.String"
    """<p>The identifier of the resource that couldn't be found.</p>"""
    resource_type: "aws_sdk_deadline.types.string.String"
    """<p>The type of the resource that couldn't be found.</p>"""
    context: NotRequired["aws_sdk_deadline.types.exception_context.ExceptionContext"]
    """<p>Information about the resources in use when the exception was thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    if "context" in value:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
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
    if "context" in data:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#ResourceNotFoundException``."""

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
