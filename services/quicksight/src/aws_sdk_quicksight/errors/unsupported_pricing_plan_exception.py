"""Generated from Smithy shape ``com.amazonaws.quicksight#UnsupportedPricingPlanException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class UnsupportedPricingPlanException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedPricingPlanException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UnsupportedPricingPlanException_:
    out: UnsupportedPricingPlanException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class UnsupportedPricingPlanException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#UnsupportedPricingPlanException``."""

    code: str | None = "UnsupportedPricingPlanException"

    def __init__(self, data: UnsupportedPricingPlanException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedPricingPlanException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedPricingPlanException":
        return cls(deserialize_json(data))
