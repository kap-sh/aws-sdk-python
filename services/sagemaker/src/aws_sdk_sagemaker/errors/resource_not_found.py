"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason


class ResourceNotFound_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFound_:
    out: ResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemaker#ResourceNotFound``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotFound":
        return cls(deserialize_aws_json_1_1(data))
