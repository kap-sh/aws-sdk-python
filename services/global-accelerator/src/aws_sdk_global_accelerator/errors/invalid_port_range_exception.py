"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#InvalidPortRangeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class InvalidPortRangeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPortRangeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPortRangeException_:
    out: InvalidPortRangeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidPortRangeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#InvalidPortRangeException``."""

    code: str | None = "InvalidPortRangeException"

    def __init__(self, data: InvalidPortRangeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPortRangeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPortRangeException":
        return cls(deserialize_aws_json_1_1(data))
