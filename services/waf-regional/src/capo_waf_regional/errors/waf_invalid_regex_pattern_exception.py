"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFInvalidRegexPatternException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf_regional.types.error_message


class WAFInvalidRegexPatternException_(TypedDict, closed=True):
    message: NotRequired["capo_waf_regional.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidRegexPatternException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidRegexPatternException_:
    out: WAFInvalidRegexPatternException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFInvalidRegexPatternException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFInvalidRegexPatternException``."""

    code: str | None = "WAFInvalidRegexPatternException"

    def __init__(self, data: WAFInvalidRegexPatternException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInvalidRegexPatternException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFInvalidRegexPatternException":
        return cls(deserialize_aws_json_1_1(data))
