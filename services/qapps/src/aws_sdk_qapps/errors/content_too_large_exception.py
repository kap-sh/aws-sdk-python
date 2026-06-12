"""Generated from Smithy shape ``com.amazonaws.qapps#ContentTooLargeException``."""

from typing import TypedDict

from aws_sdk_qapps.errors import DeserializationError, ServiceError


class ContentTooLargeException_(TypedDict):
    message: "str"
    resource_id: "str"
    """<p>The unique identifier of the resource</p>"""
    resource_type: "str"
    """<p>The type of the resource</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentTooLargeException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ContentTooLargeException_:
    out: ContentTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ContentTooLargeException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ContentTooLargeException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ContentTooLargeException_.resource_type required")
    return out


class ContentTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qapps#ContentTooLargeException``."""

    code: str | None = "ContentTooLargeException"

    def __init__(self, data: ContentTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContentTooLargeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ContentTooLargeException":
        return cls(deserialize_json(data))
