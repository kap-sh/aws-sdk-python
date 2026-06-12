"""Generated from Smithy shape ``com.amazonaws.ivschat#PendingVerification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivschat.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.error_message


class PendingVerification_(TypedDict):
    message: "aws_sdk_ivschat.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: PendingVerification_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PendingVerification_:
    out: PendingVerification_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PendingVerification_.message required")
    return out


class PendingVerification(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivschat#PendingVerification``."""

    code: str | None = "PendingVerification"

    def __init__(self, data: PendingVerification_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PendingVerification",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PendingVerification":
        return cls(deserialize_json(data))
