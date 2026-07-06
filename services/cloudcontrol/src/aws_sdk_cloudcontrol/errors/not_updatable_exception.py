"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#NotUpdatableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class NotUpdatableException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotUpdatableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotUpdatableException_:
    out: NotUpdatableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NotUpdatableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#NotUpdatableException``."""

    code: str | None = "NotUpdatableException"

    def __init__(self, data: NotUpdatableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotUpdatableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "NotUpdatableException":
        return cls(deserialize_aws_json_1_0(data))
