"""Generated from Smithy shape ``com.amazonaws.ebs#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ebs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ebs.types.access_denied_exception_reason
    import aws_sdk_ebs.types.error_message


class AccessDeniedException_(TypedDict):
    message: NotRequired["aws_sdk_ebs.types.error_message.ErrorMessage"]
    reason: (
        "aws_sdk_ebs.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    )
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    import aws_sdk_ebs.types.access_denied_exception_reason

    out["Reason"] = aws_sdk_ebs.types.access_denied_exception_reason.serialize_json(
        value["reason"]
    )
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_ebs.types.access_denied_exception_reason

        out["reason"] = (
            aws_sdk_ebs.types.access_denied_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("AccessDeniedException_.reason required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
