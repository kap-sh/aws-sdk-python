"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.service_quota_exceeded_exception_reason


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_0(data))
