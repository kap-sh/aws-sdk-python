"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#NotStabilizedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class NotStabilizedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotStabilizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotStabilizedException_:
    out: NotStabilizedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NotStabilizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#NotStabilizedException``."""

    code: str | None = "NotStabilizedException"

    def __init__(self, data: NotStabilizedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotStabilizedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "NotStabilizedException":
        return cls(deserialize_aws_json_1_0(data))
