"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ConcurrentOperationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class ConcurrentOperationException_(TypedDict):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConcurrentOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConcurrentOperationException_:
    out: ConcurrentOperationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConcurrentOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#ConcurrentOperationException``."""

    code: str | None = "ConcurrentOperationException"

    def __init__(self, data: ConcurrentOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentOperationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ConcurrentOperationException":
        return cls(deserialize_aws_json_1_0(data))
