"""Generated from Smithy shape ``com.amazonaws.wisdom#RequestTimeoutException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import ServiceError


class RequestTimeoutException_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestTimeoutException_:
    out: RequestTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RequestTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wisdom#RequestTimeoutException``."""

    code: str | None = "RequestTimeoutException"

    def __init__(self, data: RequestTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RequestTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestTimeoutException":
        return cls(deserialize_json(data))
