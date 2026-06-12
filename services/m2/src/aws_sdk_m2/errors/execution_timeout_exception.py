"""Generated from Smithy shape ``com.amazonaws.m2#ExecutionTimeoutException``."""

from typing import TypedDict

from aws_sdk_m2.errors import DeserializationError, ServiceError


class ExecutionTimeoutException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionTimeoutException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExecutionTimeoutException_:
    out: ExecutionTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ExecutionTimeoutException_.message required")
    return out


class ExecutionTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.m2#ExecutionTimeoutException``."""

    code: str | None = "ExecutionTimeoutException"

    def __init__(self, data: ExecutionTimeoutException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="ExecutionTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ExecutionTimeoutException":
        return cls(deserialize_json(data))
