"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFUnavailableEntityException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFUnavailableEntityException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFUnavailableEntityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFUnavailableEntityException_:
    out: WAFUnavailableEntityException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFUnavailableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFUnavailableEntityException``."""

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
