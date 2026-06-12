"""Generated from Smithy shape ``com.amazonaws.dsql#ConflictException``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql.errors import ServiceError

class ConflictException_(TypedDict):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>Resource Id</p>"""
    resource_type: NotRequired["str"]
    """<p>Resource Type</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dsql#ConflictException``."""
    code: str | None = 'ConflictException'

    def __init__(self, data: ConflictException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='ConflictException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))