"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConflictingOperationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.error_message
    import aws_sdk_iotsitewise.types.resource_arn
    import aws_sdk_iotsitewise.types.resource_id


class ConflictingOperationException_(TypedDict):
    message: "aws_sdk_iotsitewise.types.error_message.ErrorMessage"
    resource_id: "aws_sdk_iotsitewise.types.resource_id.ResourceId"
    """<p>The ID of the resource that conflicts with this operation.</p>"""
    resource_arn: "aws_sdk_iotsitewise.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource that conflicts with this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictingOperationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ConflictingOperationException_:
    out: ConflictingOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictingOperationException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "ConflictingOperationException_.resource_id required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "ConflictingOperationException_.resource_arn required"
        )
    return out


class ConflictingOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#ConflictingOperationException``."""

    code: str | None = "ConflictingOperationException"

    def __init__(self, data: ConflictingOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictingOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictingOperationException":
        return cls(deserialize_json(data))
