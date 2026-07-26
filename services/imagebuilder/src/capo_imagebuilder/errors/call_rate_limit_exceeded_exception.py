"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CallRateLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import capo_imagebuilder.types.error_message


class CallRateLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: CallRateLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CallRateLimitExceededException_:
    out: CallRateLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CallRateLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#CallRateLimitExceededException``."""

    code: str | None = "CallRateLimitExceededException"

    def __init__(self, data: CallRateLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CallRateLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CallRateLimitExceededException":
        return cls(deserialize_json(data))
