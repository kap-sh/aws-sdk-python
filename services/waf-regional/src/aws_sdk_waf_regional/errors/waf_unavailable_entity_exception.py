"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFUnavailableEntityException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.error_message


class WAFUnavailableEntityException_(TypedDict):
    message: NotRequired["aws_sdk_waf_regional.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFUnavailableEntityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFUnavailableEntityException_:
    out: WAFUnavailableEntityException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFUnavailableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFUnavailableEntityException``."""

    code: str | None = "WAFUnavailableEntityException"

    def __init__(self, data: WAFUnavailableEntityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFUnavailableEntityException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFUnavailableEntityException":
        return cls(deserialize_aws_json_1_1(data))
