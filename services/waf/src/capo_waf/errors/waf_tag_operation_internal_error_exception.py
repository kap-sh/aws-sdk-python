"""Generated from Smithy shape ``com.amazonaws.waf#WAFTagOperationInternalErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf.types.error_message


class WAFTagOperationInternalErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_waf.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFTagOperationInternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFTagOperationInternalErrorException_:
    out: WAFTagOperationInternalErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFTagOperationInternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.waf#WAFTagOperationInternalErrorException``."""

    code: str | None = "WAFTagOperationInternalErrorException"

    def __init__(self, data: WAFTagOperationInternalErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFTagOperationInternalErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFTagOperationInternalErrorException":
        return cls(deserialize_aws_json_1_1(data))
