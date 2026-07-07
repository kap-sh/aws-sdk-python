"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.exception_message


class QuotaExceededException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_service_quotas.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QuotaExceededException_:
    out: QuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class QuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#QuotaExceededException``."""

    code: str | None = "QuotaExceededException"

    def __init__(self, data: QuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "QuotaExceededException":
        return cls(deserialize_aws_json_1_1(data))
