"""Generated from Smithy shape ``com.amazonaws.signerdata#TooManyRequestsException``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_signer_data.errors import ServiceError

class TooManyRequestsException_(TypedDict):
    message: NotRequired["str"]
    code: NotRequired["str"]

# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signerdata#TooManyRequestsException``."""
    code: str | None = 'TooManyRequestsException'

    def __init__(self, data: TooManyRequestsException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='TooManyRequestsException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))