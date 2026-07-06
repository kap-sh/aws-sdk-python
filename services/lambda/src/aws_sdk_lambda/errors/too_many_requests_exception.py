"""Generated from Smithy shape ``com.amazonaws.lambda#TooManyRequestsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.throttle_reason


class TooManyRequestsException_(TypedDict, closed=True):
    retry_after_seconds: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The number of seconds the caller should wait before retrying.</p>"""
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]
    reason: NotRequired["aws_sdk_lambda.types.throttle_reason.ThrottleReason"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import aws_sdk_lambda.types.throttle_reason

        out["Reason"] = aws_sdk_lambda.types.throttle_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    if "Reason" in data:
        import aws_sdk_lambda.types.throttle_reason

        out["reason"] = aws_sdk_lambda.types.throttle_reason.deserialize_json(
            data["Reason"]
        )
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#TooManyRequestsException``."""

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
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))
