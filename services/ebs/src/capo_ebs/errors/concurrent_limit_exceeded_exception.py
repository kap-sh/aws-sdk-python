"""Generated from Smithy shape ``com.amazonaws.ebs#ConcurrentLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ebs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ebs.types.error_message


class ConcurrentLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ebs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConcurrentLimitExceededException_:
    out: ConcurrentLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConcurrentLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#ConcurrentLimitExceededException``."""

    code: str | None = "ConcurrentLimitExceededException"

    def __init__(self, data: ConcurrentLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConcurrentLimitExceededException":
        return cls(deserialize_json(data))
