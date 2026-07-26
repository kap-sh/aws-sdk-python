"""Generated from Smithy shape ``com.amazonaws.efs#SecurityGroupLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class SecurityGroupLimitExceeded_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupLimitExceeded_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SecurityGroupLimitExceeded_:
    out: SecurityGroupLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("SecurityGroupLimitExceeded_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SecurityGroupLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#SecurityGroupLimitExceeded``."""

    code: str | None = "SecurityGroupLimitExceeded"

    def __init__(self, data: SecurityGroupLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SecurityGroupLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SecurityGroupLimitExceeded":
        return cls(deserialize_json(data))
