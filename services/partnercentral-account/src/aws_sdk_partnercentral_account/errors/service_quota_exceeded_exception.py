"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.service_quota_exceeded_exception_reason


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    reason: "aws_sdk_partnercentral_account.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason"
    """<p>The specific reason for the service quota being exceeded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_account.types.service_quota_exceeded_exception_reason

    out["Reason"] = (
        aws_sdk_partnercentral_account.types.service_quota_exceeded_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "Reason" in data:
        import aws_sdk_partnercentral_account.types.service_quota_exceeded_exception_reason

        out["reason"] = (
            aws_sdk_partnercentral_account.types.service_quota_exceeded_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ServiceQuotaExceededException_.reason required")
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#ServiceQuotaExceededException``."""

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
