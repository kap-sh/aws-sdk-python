"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_featurestore_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.message


class ValidationError_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sagemaker_featurestore_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationError_:
    out: ValidationError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ValidationError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ValidationError``."""

    code: str | None = "ValidationError"

    def __init__(self, data: ValidationError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationError":
        return cls(deserialize_json(data))
