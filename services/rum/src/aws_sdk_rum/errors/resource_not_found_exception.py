"""Generated from Smithy shape ``com.amazonaws.rum#ResourceNotFoundException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rum.errors import DeserializationError, ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    resource_name: "str"
    """<p>The name of the resource that is associated with the error.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource that is associated with the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceName"] = value["resource_name"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_name required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rum#ResourceNotFoundException``."""

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
