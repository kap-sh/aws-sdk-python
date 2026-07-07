"""Generated from Smithy shape ``com.amazonaws.deadline#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.exception_context
    import aws_sdk_deadline.types.integer
    import aws_sdk_deadline.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_deadline.types.string.String"
    service_code: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>Identifies the service that is being throttled.</p>"""
    quota_code: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>Identifies the quota that is being throttled.</p>"""
    retry_after_seconds: NotRequired["aws_sdk_deadline.types.integer.Integer"]
    """<p>The number of seconds a client should wait before retrying the request.</p>"""
    context: NotRequired["aws_sdk_deadline.types.exception_context.ExceptionContext"]
    """<p>Information about the resources in use when the exception was thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "context" in value:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    if "context" in data:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
