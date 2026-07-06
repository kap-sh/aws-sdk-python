"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sagemakerjobruntime.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.failure_reason


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "aws_sdk_sagemakerjobruntime.types.failure_reason.FailureReason"


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerjobruntime#ServiceQuotaExceededException``."""

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
