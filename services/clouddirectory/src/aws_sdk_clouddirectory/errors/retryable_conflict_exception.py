"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RetryableConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class RetryableConflictException_(TypedDict):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RetryableConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RetryableConflictException_:
    out: RetryableConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RetryableConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#RetryableConflictException``."""

    code: str | None = "RetryableConflictException"

    def __init__(self, data: RetryableConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RetryableConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RetryableConflictException":
        return cls(deserialize_json(data))
