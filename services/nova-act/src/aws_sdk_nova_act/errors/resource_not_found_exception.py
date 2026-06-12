"""Generated from Smithy shape ``com.amazonaws.novaact#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string


class ResourceNotFoundException_(TypedDict):
    message: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The specified resource was not found.</p>"""
    resource_id: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The identifier of the resource that wasn't found.</p>"""
    resource_type: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The type of resource that wasn't found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
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
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.novaact#ResourceNotFoundException``."""

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
