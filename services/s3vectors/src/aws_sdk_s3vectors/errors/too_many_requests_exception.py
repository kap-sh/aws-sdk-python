"""Generated from Smithy shape ``com.amazonaws.s3vectors#TooManyRequestsException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.exception_message


class TooManyRequestsException_(TypedDict, closed=True):
    message: "aws_sdk_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TooManyRequestsException_.message required")
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="TooManyRequestsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))
