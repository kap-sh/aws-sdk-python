"""Generated from Smithy shape ``com.amazonaws.eventbridge#ManagedRuleException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.error_message


class ManagedRuleException_(TypedDict):
    message: NotRequired["aws_sdk_eventbridge.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleException_:
    out: ManagedRuleException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ManagedRuleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridge#ManagedRuleException``."""

    code: str | None = "ManagedRuleException"

    def __init__(self, data: ManagedRuleException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ManagedRuleException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ManagedRuleException":
        return cls(deserialize_aws_json_1_1(data))
