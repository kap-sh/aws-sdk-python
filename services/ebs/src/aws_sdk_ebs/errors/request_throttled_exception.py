"""Generated from Smithy shape ``com.amazonaws.ebs#RequestThrottledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ebs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ebs.types.error_message
    import aws_sdk_ebs.types.request_throttled_exception_reason


class RequestThrottledException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ebs.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "aws_sdk_ebs.types.request_throttled_exception_reason.RequestThrottledExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestThrottledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_ebs.types.request_throttled_exception_reason

        out["Reason"] = (
            aws_sdk_ebs.types.request_throttled_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> RequestThrottledException_:
    out: RequestThrottledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_ebs.types.request_throttled_exception_reason

        out["reason"] = (
            aws_sdk_ebs.types.request_throttled_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class RequestThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#RequestThrottledException``."""

    code: str | None = "RequestThrottledException"

    def __init__(self, data: RequestThrottledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestThrottledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestThrottledException":
        return cls(deserialize_json(data))
