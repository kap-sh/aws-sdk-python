"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message
    import capo_iotsitewise.types.resource_arn
    import capo_iotsitewise.types.resource_id


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    message: "capo_iotsitewise.types.error_message.ErrorMessage"
    resource_id: "capo_iotsitewise.types.resource_id.ResourceId"
    """<p>The ID of the resource that already exists.</p>"""
    resource_arn: "capo_iotsitewise.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource that already exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceAlreadyExistsException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "ResourceAlreadyExistsException_.resource_id required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "ResourceAlreadyExistsException_.resource_arn required"
        )
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#ResourceAlreadyExistsException``."""

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
