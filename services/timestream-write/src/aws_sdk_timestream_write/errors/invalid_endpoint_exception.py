"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#InvalidEndpointException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.error_message


class InvalidEndpointException_(TypedDict):
    message: NotRequired["aws_sdk_timestream_write.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidEndpointException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidEndpointException_:
    out: InvalidEndpointException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidEndpointException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.timestreamwrite#InvalidEndpointException``."""

    code: str | None = "InvalidEndpointException"

    def __init__(self, data: InvalidEndpointException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEndpointException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidEndpointException":
        return cls(deserialize_aws_json_1_0(data))
