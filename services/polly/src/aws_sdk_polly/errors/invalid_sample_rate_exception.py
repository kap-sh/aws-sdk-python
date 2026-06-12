"""Generated from Smithy shape ``com.amazonaws.polly#InvalidSampleRateException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class InvalidSampleRateException_(TypedDict):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidSampleRateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidSampleRateException_:
    out: InvalidSampleRateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidSampleRateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#InvalidSampleRateException``."""

    code: str | None = "InvalidSampleRateException"

    def __init__(self, data: InvalidSampleRateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSampleRateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidSampleRateException":
        return cls(deserialize_json(data))
