"""Generated from Smithy shape ``com.amazonaws.xray#PolicySizeLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import ServiceError

if TYPE_CHECKING:
    import capo_xray.types.error_message


class PolicySizeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicySizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicySizeLimitExceededException_:
    out: PolicySizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicySizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#PolicySizeLimitExceededException``."""

    code: str | None = "PolicySizeLimitExceededException"

    def __init__(self, data: PolicySizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicySizeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PolicySizeLimitExceededException":
        return cls(deserialize_json(data))
