"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFLimitsExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_wafv2.types.error_message
    import capo_wafv2.types.source_type


class WAFLimitsExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_wafv2.types.error_message.ErrorMessage"]
    source_type: NotRequired["capo_wafv2.types.source_type.SourceType"]
    """<p>Source type for the exception. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFLimitsExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFLimitsExceededException_:
    out: WAFLimitsExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    return out


class WAFLimitsExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFLimitsExceededException``."""

    code: str | None = "WAFLimitsExceededException"

    def __init__(self, data: WAFLimitsExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFLimitsExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFLimitsExceededException":
        return cls(deserialize_aws_json_1_1(data))
