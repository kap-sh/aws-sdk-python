"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFBadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf_regional.types.error_message


class WAFBadRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_waf_regional.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFBadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFBadRequestException_:
    out: WAFBadRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFBadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFBadRequestException``."""

    code: str | None = "WAFBadRequestException"

    def __init__(self, data: WAFBadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFBadRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFBadRequestException":
        return cls(deserialize_aws_json_1_1(data))
