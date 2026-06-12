"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ClientLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_archived_media.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.error_message


class ClientLimitExceededException_(TypedDict):
    message: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ClientLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ClientLimitExceededException_:
    out: ClientLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ClientLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ClientLimitExceededException``."""

    code: str | None = "ClientLimitExceededException"

    def __init__(self, data: ClientLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClientLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ClientLimitExceededException":
        return cls(deserialize_json(data))
