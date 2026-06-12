"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ResourceNotFoundException``."""

from typing import TypedDict
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances.errors import ServiceError

class ResourceNotFoundException_(TypedDict):
    message: "str"
    """<p>Details about the missing resource.</p>"""
    resource_id: "str"
    """<p>Identifier of the resource that was not found.</p>"""
    resource_type: "str"
    """<p>Type of the resource that was not found.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#ResourceNotFoundException``."""
    code: str | None = 'ResourceNotFoundException'

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='ResourceNotFoundException')
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data))