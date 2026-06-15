"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RetryableConflictException``."""

from typing import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, ServiceError


class RetryableConflictException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RetryableConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RetryableConflictException_:
    out: RetryableConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RetryableConflictException_.message required")
    return out


class RetryableConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#RetryableConflictException``."""

    code: str | None = "RetryableConflictException"

    def __init__(self, data: RetryableConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RetryableConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RetryableConflictException":
        return cls(deserialize_json(data))
