"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardsPerClusterQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class ShardsPerClusterQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardsPerClusterQuotaExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShardsPerClusterQuotaExceededFault_:
    out: ShardsPerClusterQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ShardsPerClusterQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#ShardsPerClusterQuotaExceededFault``."""

    code: str | None = "ShardsPerClusterQuotaExceededFault"

    def __init__(self, data: ShardsPerClusterQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ShardsPerClusterQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ShardsPerClusterQuotaExceededFault":
        return cls(deserialize_aws_json_1_1(data))
