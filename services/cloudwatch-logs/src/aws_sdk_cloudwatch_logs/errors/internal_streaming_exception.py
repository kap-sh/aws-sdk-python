"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InternalStreamingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.message


class InternalStreamingException_(TypedDict):
    message: NotRequired["aws_sdk_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalStreamingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalStreamingException_:
    out: InternalStreamingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalStreamingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#InternalStreamingException``."""

    code: str | None = "InternalStreamingException"

    def __init__(self, data: InternalStreamingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalStreamingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalStreamingException":
        return cls(deserialize_aws_json_1_1(data))
