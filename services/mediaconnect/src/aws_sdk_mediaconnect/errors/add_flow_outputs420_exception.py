"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowOutputs420Exception``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_mediaconnect.errors import ServiceError

class AddFlowOutputs420Exception_(TypedDict):
    message: NotRequired["str"]

# --- restJson1 ser/de ---
def serialize_json(value: AddFlowOutputs420Exception_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AddFlowOutputs420Exception_:
    out: AddFlowOutputs420Exception_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AddFlowOutputs420Exception(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#AddFlowOutputs420Exception``."""
    code: str | None = 'AddFlowOutputs420Exception'

    def __init__(self, data: AddFlowOutputs420Exception_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='AddFlowOutputs420Exception')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AddFlowOutputs420Exception":
        return cls(deserialize_json(data))