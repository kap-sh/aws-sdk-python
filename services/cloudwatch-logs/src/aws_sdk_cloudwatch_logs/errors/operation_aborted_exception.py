"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OperationAbortedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.message


class OperationAbortedException_(TypedDict):
    message: NotRequired["aws_sdk_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationAbortedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationAbortedException_:
    out: OperationAbortedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OperationAbortedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#OperationAbortedException``."""

    code: str | None = "OperationAbortedException"

    def __init__(self, data: OperationAbortedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationAbortedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OperationAbortedException":
        return cls(deserialize_aws_json_1_1(data))
