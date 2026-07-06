"""Generated from Smithy shape ``com.amazonaws.polly#InvalidS3KeyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class InvalidS3KeyException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidS3KeyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidS3KeyException_:
    out: InvalidS3KeyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidS3KeyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#InvalidS3KeyException``."""

    code: str | None = "InvalidS3KeyException"

    def __init__(self, data: InvalidS3KeyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3KeyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidS3KeyException":
        return cls(deserialize_json(data))
