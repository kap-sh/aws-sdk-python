"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.server_side_string


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    resource_id: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The ID of the resource.</p>"""
    resource_type: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#ConflictException``."""

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
