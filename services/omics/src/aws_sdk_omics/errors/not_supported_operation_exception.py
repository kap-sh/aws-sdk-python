"""Generated from Smithy shape ``com.amazonaws.omics#NotSupportedOperationException``."""

from typing import TypedDict

from aws_sdk_omics.errors import DeserializationError, ServiceError


class NotSupportedOperationException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NotSupportedOperationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotSupportedOperationException_:
    out: NotSupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotSupportedOperationException_.message required")
    return out


class NotSupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.omics#NotSupportedOperationException``."""

    code: str | None = "NotSupportedOperationException"

    def __init__(self, data: NotSupportedOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotSupportedOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotSupportedOperationException":
        return cls(deserialize_json(data))
