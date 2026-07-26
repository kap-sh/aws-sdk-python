"""Generated from Smithy shape ``com.amazonaws.efs#PolicyNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class PolicyNotFound_(TypedDict, closed=True):
    error_code: NotRequired["capo_efs.types.error_code.ErrorCode"]
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyNotFound_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyNotFound_:
    out: PolicyNotFound_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#PolicyNotFound``."""

    code: str | None = "PolicyNotFound"

    def __init__(self, data: PolicyNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyNotFound",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PolicyNotFound":
        return cls(deserialize_json(data))
