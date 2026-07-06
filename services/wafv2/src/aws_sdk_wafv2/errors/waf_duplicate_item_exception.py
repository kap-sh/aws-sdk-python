"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFDuplicateItemException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFDuplicateItemException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFDuplicateItemException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFDuplicateItemException_:
    out: WAFDuplicateItemException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFDuplicateItemException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFDuplicateItemException``."""

    code: str | None = "WAFDuplicateItemException"

    def __init__(self, data: WAFDuplicateItemException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFDuplicateItemException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFDuplicateItemException":
        return cls(deserialize_aws_json_1_1(data))
