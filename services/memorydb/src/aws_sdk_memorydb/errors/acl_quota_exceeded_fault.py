"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class ACLQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLQuotaExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ACLQuotaExceededFault_:
    out: ACLQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ACLQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#ACLQuotaExceededFault``."""

    code: str | None = "ACLQuotaExceededFault"

    def __init__(self, data: ACLQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ACLQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ACLQuotaExceededFault":
        return cls(deserialize_aws_json_1_1(data))
