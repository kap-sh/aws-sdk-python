"""Generated from Smithy shape ``com.amazonaws.s3vectors#RequestTimeoutException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.exception_message


class RequestTimeoutException_(TypedDict, closed=True):
    message: "aws_sdk_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: RequestTimeoutException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestTimeoutException_:
    out: RequestTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RequestTimeoutException_.message required")
    return out


class RequestTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#RequestTimeoutException``."""

    code: str | None = "RequestTimeoutException"

    def __init__(self, data: RequestTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RequestTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestTimeoutException":
        return cls(deserialize_json(data))
