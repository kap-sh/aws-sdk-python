"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ResourceNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_featurestore_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.message


class ResourceNotFound_(TypedDict):
    message: NotRequired["aws_sdk_sagemaker_featurestore_runtime.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFound_:
    out: ResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ResourceNotFound``."""

    code: str | None = "ResourceNotFound"

    def __init__(self, data: ResourceNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFound",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFound":
        return cls(deserialize_json(data))
