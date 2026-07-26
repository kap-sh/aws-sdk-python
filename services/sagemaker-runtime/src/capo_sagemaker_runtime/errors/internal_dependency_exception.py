"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InternalDependencyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemaker_runtime.types.message


class InternalDependencyException_(TypedDict, closed=True):
    message: NotRequired["capo_sagemaker_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalDependencyException_:
    out: InternalDependencyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntime#InternalDependencyException``."""

    code: str | None = "InternalDependencyException"

    def __init__(self, data: InternalDependencyException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalDependencyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalDependencyException":
        return cls(deserialize_json(data))
