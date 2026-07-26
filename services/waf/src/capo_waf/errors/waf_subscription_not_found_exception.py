"""Generated from Smithy shape ``com.amazonaws.waf#WAFSubscriptionNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf.types.error_message


class WAFSubscriptionNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_waf.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFSubscriptionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFSubscriptionNotFoundException_:
    out: WAFSubscriptionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFSubscriptionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.waf#WAFSubscriptionNotFoundException``."""

    code: str | None = "WAFSubscriptionNotFoundException"

    def __init__(self, data: WAFSubscriptionNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFSubscriptionNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFSubscriptionNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
