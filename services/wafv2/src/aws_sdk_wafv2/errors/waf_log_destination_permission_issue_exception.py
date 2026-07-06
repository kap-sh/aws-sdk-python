"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFLogDestinationPermissionIssueException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message


class WAFLogDestinationPermissionIssueException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFLogDestinationPermissionIssueException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFLogDestinationPermissionIssueException_:
    out: WAFLogDestinationPermissionIssueException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class WAFLogDestinationPermissionIssueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFLogDestinationPermissionIssueException``."""

    code: str | None = "WAFLogDestinationPermissionIssueException"

    def __init__(self, data: WAFLogDestinationPermissionIssueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFLogDestinationPermissionIssueException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "WAFLogDestinationPermissionIssueException":
        return cls(deserialize_aws_json_1_1(data))
