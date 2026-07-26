"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#InvalidMediaFrameException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.error_message


class InvalidMediaFrameException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidMediaFrameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidMediaFrameException_:
    out: InvalidMediaFrameException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidMediaFrameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#InvalidMediaFrameException``."""

    code: str | None = "InvalidMediaFrameException"

    def __init__(self, data: InvalidMediaFrameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidMediaFrameException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidMediaFrameException":
        return cls(deserialize_json(data))
