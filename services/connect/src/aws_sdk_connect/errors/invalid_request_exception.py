"""Generated from Smithy shape ``com.amazonaws.connect#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.invalid_request_exception_reason
    import aws_sdk_connect.types.message


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_connect.types.message.Message"]
    """<p>The message about the request.</p>"""
    reason: NotRequired[
        "aws_sdk_connect.types.invalid_request_exception_reason.InvalidRequestExceptionReason"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_connect.types.invalid_request_exception_reason

        out["Reason"] = (
            aws_sdk_connect.types.invalid_request_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_connect.types.invalid_request_exception_reason

        out["reason"] = (
            aws_sdk_connect.types.invalid_request_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_json(data))
