"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateGateway420Exception``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_mediaconnect.errors import ServiceError

class CreateGateway420Exception_(TypedDict):
    message: NotRequired["str"]

# --- restJson1 ser/de ---
def serialize_json(value: CreateGateway420Exception_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateGateway420Exception_:
    out: CreateGateway420Exception_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CreateGateway420Exception(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#CreateGateway420Exception``."""
    code: str | None = 'CreateGateway420Exception'

    def __init__(self, data: CreateGateway420Exception_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='CreateGateway420Exception')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CreateGateway420Exception":
        return cls(deserialize_json(data))