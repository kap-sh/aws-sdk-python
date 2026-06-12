"""Generated from Smithy shape ``com.amazonaws.waf#WAFInternalErrorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_waf.types.error_message


class WAFInternalErrorException_(TypedDict):
    message: NotRequired["aws_sdk_waf.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInternalErrorException_:
    out: WAFInternalErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFInternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.waf#WAFInternalErrorException``."""

    code: str | None = "WAFInternalErrorException"

    def __init__(self, data: WAFInternalErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInternalErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFInternalErrorException":
        return cls(deserialize_aws_json_1_1(data))
