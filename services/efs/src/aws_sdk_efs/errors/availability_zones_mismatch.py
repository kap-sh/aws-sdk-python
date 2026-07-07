"""Generated from Smithy shape ``com.amazonaws.efs#AvailabilityZonesMismatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message


class AvailabilityZonesMismatch_(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_efs.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZonesMismatch_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AvailabilityZonesMismatch_:
    out: AvailabilityZonesMismatch_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AvailabilityZonesMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#AvailabilityZonesMismatch``."""

    code: str | None = "AvailabilityZonesMismatch"

    def __init__(self, data: AvailabilityZonesMismatch_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AvailabilityZonesMismatch",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AvailabilityZonesMismatch":
        return cls(deserialize_json(data))
