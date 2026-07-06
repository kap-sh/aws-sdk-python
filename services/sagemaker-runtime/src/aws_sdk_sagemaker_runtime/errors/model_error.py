"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#ModelError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.log_stream_arn
    import aws_sdk_sagemaker_runtime.types.message
    import aws_sdk_sagemaker_runtime.types.status_code


class ModelError_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sagemaker_runtime.types.message.Message"]
    original_status_code: NotRequired[
        "aws_sdk_sagemaker_runtime.types.status_code.StatusCode"
    ]
    """<p> Original status code. </p>"""
    original_message: NotRequired["aws_sdk_sagemaker_runtime.types.message.Message"]
    """<p> Original message. </p>"""
    log_stream_arn: NotRequired[
        "aws_sdk_sagemaker_runtime.types.log_stream_arn.LogStreamArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the log stream. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "original_status_code" in value:
        out["OriginalStatusCode"] = value["original_status_code"]
    if "original_message" in value:
        out["OriginalMessage"] = value["original_message"]
    if "log_stream_arn" in value:
        out["LogStreamArn"] = value["log_stream_arn"]
    return out


def deserialize_json(data: dict) -> ModelError_:
    out: ModelError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "OriginalStatusCode" in data:
        out["original_status_code"] = data["OriginalStatusCode"]
    if "OriginalMessage" in data:
        out["original_message"] = data["OriginalMessage"]
    if "LogStreamArn" in data:
        out["log_stream_arn"] = data["LogStreamArn"]
    return out


class ModelError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#ModelError``."""

    code: str | None = "ModelError"

    def __init__(self, data: ModelError_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="ModelError"
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelError":
        return cls(deserialize_json(data))
