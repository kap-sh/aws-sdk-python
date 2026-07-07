"""Generated from Smithy shape ``com.amazonaws.athena#TooManyRequestsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_athena.types.error_message
    import aws_sdk_athena.types.throttle_reason


class TooManyRequestsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]
    reason: NotRequired["aws_sdk_athena.types.throttle_reason.ThrottleReason"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_athena.types.throttle_reason

        out["Reason"] = aws_sdk_athena.types.throttle_reason.serialize_aws_json_1_1(
            value["reason"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_athena.types.throttle_reason

        out["reason"] = aws_sdk_athena.types.throttle_reason.deserialize_aws_json_1_1(
            data["Reason"]
        )
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.athena#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequestsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_aws_json_1_1(data))
