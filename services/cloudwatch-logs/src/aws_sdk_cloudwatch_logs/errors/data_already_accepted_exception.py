"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataAlreadyAcceptedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.message
    import aws_sdk_cloudwatch_logs.types.sequence_token


class DataAlreadyAcceptedException_(TypedDict):
    expected_sequence_token: NotRequired[
        "aws_sdk_cloudwatch_logs.types.sequence_token.SequenceToken"
    ]
    message: NotRequired["aws_sdk_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataAlreadyAcceptedException_) -> dict:
    out: dict = {}
    if "expected_sequence_token" in value:
        out["expectedSequenceToken"] = value["expected_sequence_token"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataAlreadyAcceptedException_:
    out: DataAlreadyAcceptedException_ = {}  # type: ignore[typeddict-item]
    if "expectedSequenceToken" in data:
        out["expected_sequence_token"] = data["expectedSequenceToken"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DataAlreadyAcceptedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#DataAlreadyAcceptedException``."""

    code: str | None = "DataAlreadyAcceptedException"

    def __init__(self, data: DataAlreadyAcceptedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataAlreadyAcceptedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DataAlreadyAcceptedException":
        return cls(deserialize_aws_json_1_1(data))
