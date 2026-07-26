"""Generated from Smithy shape ``com.amazonaws.memorydb#APICallRateForCustomerExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.exception_message


class APICallRateForCustomerExceededFault_(TypedDict, closed=True):
    message: NotRequired["capo_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: APICallRateForCustomerExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> APICallRateForCustomerExceededFault_:
    out: APICallRateForCustomerExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class APICallRateForCustomerExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#APICallRateForCustomerExceededFault``."""

    code: str | None = "APICallRateForCustomerExceededFault"

    def __init__(self, data: APICallRateForCustomerExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="APICallRateForCustomerExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "APICallRateForCustomerExceededFault":
        return cls(deserialize_aws_json_1_1(data))
