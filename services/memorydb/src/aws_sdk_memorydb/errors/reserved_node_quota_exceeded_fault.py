"""Generated from Smithy shape ``com.amazonaws.memorydb#ReservedNodeQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class ReservedNodeQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedNodeQuotaExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedNodeQuotaExceededFault_:
    out: ReservedNodeQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ReservedNodeQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#ReservedNodeQuotaExceededFault``."""

    code: str | None = "ReservedNodeQuotaExceededFault"

    def __init__(self, data: ReservedNodeQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReservedNodeQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ReservedNodeQuotaExceededFault":
        return cls(deserialize_aws_json_1_1(data))
