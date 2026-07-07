"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFExpiredManagedRuleGroupVersionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFExpiredManagedRuleGroupVersionException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFExpiredManagedRuleGroupVersionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFExpiredManagedRuleGroupVersionException_:
    out: WAFExpiredManagedRuleGroupVersionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFExpiredManagedRuleGroupVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFExpiredManagedRuleGroupVersionException``."""

    code: str | None = "WAFExpiredManagedRuleGroupVersionException"

    def __init__(self, data: WAFExpiredManagedRuleGroupVersionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFExpiredManagedRuleGroupVersionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "WAFExpiredManagedRuleGroupVersionException":
        return cls(deserialize_aws_json_1_1(data))
