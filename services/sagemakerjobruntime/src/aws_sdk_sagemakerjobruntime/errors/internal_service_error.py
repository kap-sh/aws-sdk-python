"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#InternalServiceError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemakerjobruntime.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.failure_reason


class InternalServiceError_(TypedDict):
    message: "aws_sdk_sagemakerjobruntime.types.failure_reason.FailureReason"


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceError_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceError_:
    out: InternalServiceError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServiceError_.message required")
    return out


class InternalServiceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerjobruntime#InternalServiceError``."""

    code: str | None = "InternalServiceError"

    def __init__(self, data: InternalServiceError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServiceError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServiceError":
        return cls(deserialize_json(data))
