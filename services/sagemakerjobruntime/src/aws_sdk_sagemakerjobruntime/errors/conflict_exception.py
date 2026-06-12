"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemakerjobruntime.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.failure_reason


class ConflictException_(TypedDict):
    message: "aws_sdk_sagemakerjobruntime.types.failure_reason.FailureReason"


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerjobruntime#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
