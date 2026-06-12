"""Generated from Smithy shape ``com.amazonaws.iot#InvalidResponseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class InvalidResponseException_(TypedDict):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidResponseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidResponseException_:
    out: InvalidResponseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidResponseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#InvalidResponseException``."""

    code: str | None = "InvalidResponseException"

    def __init__(self, data: InvalidResponseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResponseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidResponseException":
        return cls(deserialize_json(data))
