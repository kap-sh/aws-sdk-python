"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#ModelNotReadyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.message


class ModelNotReadyException_(TypedDict, closed=True):
    message: NotRequired["capo_sagemaker_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ModelNotReadyException_:
    out: ModelNotReadyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ModelNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#ModelNotReadyException``."""

    code: str | None = "ModelNotReadyException"

    def __init__(self, data: ModelNotReadyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelNotReadyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelNotReadyException":
        return cls(deserialize_json(data))
