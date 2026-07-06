"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#UnsupportedStreamMediaTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.error_message


class UnsupportedStreamMediaTypeException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedStreamMediaTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedStreamMediaTypeException_:
    out: UnsupportedStreamMediaTypeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedStreamMediaTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#UnsupportedStreamMediaTypeException``."""

    code: str | None = "UnsupportedStreamMediaTypeException"

    def __init__(self, data: UnsupportedStreamMediaTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedStreamMediaTypeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedStreamMediaTypeException":
        return cls(deserialize_json(data))
