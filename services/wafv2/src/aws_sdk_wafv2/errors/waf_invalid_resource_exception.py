"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFInvalidResourceException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFInvalidResourceException_(TypedDict):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidResourceException_:
    out: WAFInvalidResourceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFInvalidResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFInvalidResourceException``."""

    code: str | None = "WAFInvalidResourceException"

    def __init__(self, data: WAFInvalidResourceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInvalidResourceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFInvalidResourceException":
        return cls(deserialize_aws_json_1_1(data))
