"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#NoDataRetentionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.error_message


class NoDataRetentionException_(TypedDict):
    message: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: NoDataRetentionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoDataRetentionException_:
    out: NoDataRetentionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NoDataRetentionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#NoDataRetentionException``."""

    code: str | None = "NoDataRetentionException"

    def __init__(self, data: NoDataRetentionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoDataRetentionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NoDataRetentionException":
        return cls(deserialize_json(data))
