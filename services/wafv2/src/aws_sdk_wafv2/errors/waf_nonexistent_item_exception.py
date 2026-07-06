"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFNonexistentItemException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFNonexistentItemException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFNonexistentItemException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFNonexistentItemException_:
    out: WAFNonexistentItemException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFNonexistentItemException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFNonexistentItemException``."""

    code: str | None = "WAFNonexistentItemException"

    def __init__(self, data: WAFNonexistentItemException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFNonexistentItemException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFNonexistentItemException":
        return cls(deserialize_aws_json_1_1(data))
