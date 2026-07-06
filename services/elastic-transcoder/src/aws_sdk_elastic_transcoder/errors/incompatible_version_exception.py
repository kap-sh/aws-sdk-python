"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#IncompatibleVersionException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_transcoder.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.exception_message


class IncompatibleVersionException_(TypedDict, closed=True):
    message: "aws_sdk_elastic_transcoder.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleVersionException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IncompatibleVersionException_:
    out: IncompatibleVersionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("IncompatibleVersionException_.message required")
    return out


class IncompatibleVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elastictranscoder#IncompatibleVersionException``."""

    code: str | None = "IncompatibleVersionException"

    def __init__(self, data: IncompatibleVersionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleVersionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IncompatibleVersionException":
        return cls(deserialize_json(data))
