"""Generated from Smithy shape ``com.amazonaws.efs#ThroughputLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message


class ThroughputLimitExceeded_(TypedDict, closed=True):
    error_code: "aws_sdk_efs.types.error_code.ErrorCode"
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ThroughputLimitExceeded_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThroughputLimitExceeded_:
    out: ThroughputLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("ThroughputLimitExceeded_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ThroughputLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#ThroughputLimitExceeded``."""

    code: str | None = "ThroughputLimitExceeded"

    def __init__(self, data: ThroughputLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThroughputLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThroughputLimitExceeded":
        return cls(deserialize_json(data))
