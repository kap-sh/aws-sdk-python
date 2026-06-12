"""Generated from Smithy shape ``com.amazonaws.iotdataplane#UnsupportedDocumentEncodingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.error_message


class UnsupportedDocumentEncodingException_(TypedDict):
    message: NotRequired["aws_sdk_iot_data_plane.types.error_message.errorMessage"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedDocumentEncodingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedDocumentEncodingException_:
    out: UnsupportedDocumentEncodingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedDocumentEncodingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotdataplane#UnsupportedDocumentEncodingException``."""

    code: str | None = "UnsupportedDocumentEncodingException"

    def __init__(self, data: UnsupportedDocumentEncodingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedDocumentEncodingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedDocumentEncodingException":
        return cls(deserialize_json(data))
