"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InternalServerException``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances.errors import ServiceError

class InternalServerException_(TypedDict):
    message: "str"
    """<p>Description of the internal server error.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>Recommended wait time before retrying the request.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#InternalServerException``."""
    code: str | None = 'InternalServerException'

    def __init__(self, data: InternalServerException_):
        super().__init__('server', is_throttling_error=False, is_retryable=True, code='InternalServerException')
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data))