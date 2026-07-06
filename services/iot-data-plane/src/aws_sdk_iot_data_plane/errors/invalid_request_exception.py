"""Generated from Smithy shape ``com.amazonaws.iotdataplane#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.error_message


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iot_data_plane.types.error_message.errorMessage"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotdataplane#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_json(data))
