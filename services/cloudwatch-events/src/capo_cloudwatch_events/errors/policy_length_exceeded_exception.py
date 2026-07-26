"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PolicyLengthExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.error_message


class PolicyLengthExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch_events.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyLengthExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyLengthExceededException_:
    out: PolicyLengthExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PolicyLengthExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchevents#PolicyLengthExceededException``."""

    code: str | None = "PolicyLengthExceededException"

    def __init__(self, data: PolicyLengthExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyLengthExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PolicyLengthExceededException":
        return cls(deserialize_aws_json_1_1(data))
