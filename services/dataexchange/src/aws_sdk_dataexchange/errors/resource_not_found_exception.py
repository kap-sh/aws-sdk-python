"""Generated from Smithy shape ``com.amazonaws.dataexchange#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The resource couldn't be found.</p>"""
    resource_id: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The unique identifier for the resource that couldn't be found.</p>"""
    resource_type: NotRequired["aws_sdk_dataexchange.types.resource_type.ResourceType"]
    """<p>The type of resource that couldn't be found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dataexchange#ResourceNotFoundException``."""

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
