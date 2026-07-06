"""Generated from Smithy shape ``com.amazonaws.codeartifact#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeartifact.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.resource_type
    import aws_sdk_codeartifact.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_codeartifact.types.string.String"
    resource_id: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The ID of the resource. </p>"""
    resource_type: NotRequired["aws_sdk_codeartifact.types.resource_type.ResourceType"]
    """<p> The type of Amazon Web Services resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_codeartifact.types.resource_type

        out["resourceType"] = aws_sdk_codeartifact.types.resource_type.serialize_json(
            value["resource_type"]
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
    if "resourceType" in data:
        import aws_sdk_codeartifact.types.resource_type

        out["resource_type"] = (
            aws_sdk_codeartifact.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeartifact#ResourceNotFoundException``."""

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
