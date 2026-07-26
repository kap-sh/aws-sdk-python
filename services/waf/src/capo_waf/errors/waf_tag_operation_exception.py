"""Generated from Smithy shape ``com.amazonaws.waf#WAFTagOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf.types.error_message


class WAFTagOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_waf.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFTagOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFTagOperationException_:
    out: WAFTagOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFTagOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.waf#WAFTagOperationException``."""

    code: str | None = "WAFTagOperationException"

    def __init__(self, data: WAFTagOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFTagOperationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFTagOperationException":
        return cls(deserialize_aws_json_1_1(data))
