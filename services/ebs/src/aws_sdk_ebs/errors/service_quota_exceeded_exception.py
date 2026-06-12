"""Generated from Smithy shape ``com.amazonaws.ebs#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ebs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ebs.types.error_message
    import aws_sdk_ebs.types.service_quota_exceeded_exception_reason


class ServiceQuotaExceededException_(TypedDict):
    message: NotRequired["aws_sdk_ebs.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "aws_sdk_ebs.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_ebs.types.service_quota_exceeded_exception_reason

        out["Reason"] = (
            aws_sdk_ebs.types.service_quota_exceeded_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_ebs.types.service_quota_exceeded_exception_reason

        out["reason"] = (
            aws_sdk_ebs.types.service_quota_exceeded_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#ServiceQuotaExceededException``."""

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
    def from_json(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data))
