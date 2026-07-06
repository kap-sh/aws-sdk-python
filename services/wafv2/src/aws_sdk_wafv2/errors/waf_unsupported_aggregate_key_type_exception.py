"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFUnsupportedAggregateKeyTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFUnsupportedAggregateKeyTypeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFUnsupportedAggregateKeyTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFUnsupportedAggregateKeyTypeException_:
    out: WAFUnsupportedAggregateKeyTypeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFUnsupportedAggregateKeyTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFUnsupportedAggregateKeyTypeException``."""

    code: str | None = "WAFUnsupportedAggregateKeyTypeException"

    def __init__(self, data: WAFUnsupportedAggregateKeyTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFUnsupportedAggregateKeyTypeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFUnsupportedAggregateKeyTypeException":
        return cls(deserialize_aws_json_1_1(data))
