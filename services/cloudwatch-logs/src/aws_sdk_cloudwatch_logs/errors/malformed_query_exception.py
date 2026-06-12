"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MalformedQueryException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.message
    import aws_sdk_cloudwatch_logs.types.query_compile_error


class MalformedQueryException_(TypedDict):
    query_compile_error: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_compile_error.QueryCompileError"
    ]
    message: NotRequired["aws_sdk_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MalformedQueryException_) -> dict:
    out: dict = {}
    if "query_compile_error" in value:
        import aws_sdk_cloudwatch_logs.types.query_compile_error

        out["queryCompileError"] = (
            aws_sdk_cloudwatch_logs.types.query_compile_error.serialize_aws_json_1_1(
                value["query_compile_error"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MalformedQueryException_:
    out: MalformedQueryException_ = {}  # type: ignore[typeddict-item]
    if "queryCompileError" in data:
        import aws_sdk_cloudwatch_logs.types.query_compile_error

        out["query_compile_error"] = (
            aws_sdk_cloudwatch_logs.types.query_compile_error.deserialize_aws_json_1_1(
                data["queryCompileError"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out


class MalformedQueryException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#MalformedQueryException``."""

    code: str | None = "MalformedQueryException"

    def __init__(self, data: MalformedQueryException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedQueryException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MalformedQueryException":
        return cls(deserialize_aws_json_1_1(data))
