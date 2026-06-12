"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InternalFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.message


class InternalFailure_(TypedDict):
    message: NotRequired["aws_sdk_sagemaker_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalFailure_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalFailure_:
    out: InternalFailure_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#InternalFailure``."""

    code: str | None = "InternalFailure"

    def __init__(self, data: InternalFailure_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailure",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalFailure":
        return cls(deserialize_json(data))
