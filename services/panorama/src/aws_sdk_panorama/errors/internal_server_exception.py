"""Generated from Smithy shape ``com.amazonaws.panorama#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_panorama.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.retry_after_seconds
    import aws_sdk_panorama.types.string


class InternalServerException_(TypedDict):
    message: "aws_sdk_panorama.types.string.String"
    retry_after_seconds: "aws_sdk_panorama.types.retry_after_seconds.RetryAfterSeconds"
    """<p>The number of seconds a client should wait before retrying the call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.panorama#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
