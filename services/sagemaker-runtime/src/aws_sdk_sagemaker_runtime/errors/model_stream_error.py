"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#ModelStreamError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.error_code
    import aws_sdk_sagemaker_runtime.types.message


class ModelStreamError_(TypedDict):
    message: NotRequired["aws_sdk_sagemaker_runtime.types.message.Message"]
    error_code: NotRequired["aws_sdk_sagemaker_runtime.types.error_code.ErrorCode"]
    """<p>This error can have the following error codes:</p> <dl> <dt>ModelInvocationTimeExceeded</dt> <dd> <p>The model failed to finish sending the response within the timeout period allowed by Amazon SageMaker AI.</p> </dd> <dt>StreamBroken</dt> <dd> <p>The Transmission Control Protocol (TCP) connection between the client and the model was reset or closed.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelStreamError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ModelStreamError_:
    out: ModelStreamError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out


class ModelStreamError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#ModelStreamError``."""

    code: str | None = "ModelStreamError"

    def __init__(self, data: ModelStreamError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelStreamError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelStreamError":
        return cls(deserialize_json(data))
