"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#InternalServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_transcoder.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.exception_message


class InternalServiceException_(TypedDict, closed=True):
    message: "aws_sdk_elastic_transcoder.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceException_:
    out: InternalServiceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServiceException_.message required")
    return out


class InternalServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elastictranscoder#InternalServiceException``."""

    code: str | None = "InternalServiceException"

    def __init__(self, data: InternalServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServiceException":
        return cls(deserialize_json(data))
