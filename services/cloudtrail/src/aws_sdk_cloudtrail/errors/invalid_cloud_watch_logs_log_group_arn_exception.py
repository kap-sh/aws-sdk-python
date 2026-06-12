"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InvalidCloudWatchLogsLogGroupArnException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class InvalidCloudWatchLogsLogGroupArnException_(TypedDict):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCloudWatchLogsLogGroupArnException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidCloudWatchLogsLogGroupArnException_:
    out: InvalidCloudWatchLogsLogGroupArnException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidCloudWatchLogsLogGroupArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InvalidCloudWatchLogsLogGroupArnException``."""

    code: str | None = "InvalidCloudWatchLogsLogGroupArnException"

    def __init__(self, data: InvalidCloudWatchLogsLogGroupArnException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCloudWatchLogsLogGroupArnException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidCloudWatchLogsLogGroupArnException":
        return cls(deserialize_aws_json_1_1(data))
