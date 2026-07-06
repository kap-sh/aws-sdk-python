"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.access_denied_exception_reason


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccessDeniedException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data))
