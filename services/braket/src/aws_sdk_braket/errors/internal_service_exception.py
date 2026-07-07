"""Generated from Smithy shape ``com.amazonaws.braket#InternalServiceException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import ServiceError


class InternalServiceException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceException_:
    out: InternalServiceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.braket#InternalServiceException``."""

    code: str | None = "InternalServiceException"

    def __init__(self, data: InternalServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServiceException":
        return cls(deserialize_json(data))
