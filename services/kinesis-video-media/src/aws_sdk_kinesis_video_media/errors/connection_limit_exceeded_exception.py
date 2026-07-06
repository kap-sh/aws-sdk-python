"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#ConnectionLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video_media.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_media.types.error_message


class ConnectionLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kinesis_video_media.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectionLimitExceededException_:
    out: ConnectionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConnectionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideomedia#ConnectionLimitExceededException``."""

    code: str | None = "ConnectionLimitExceededException"

    def __init__(self, data: ConnectionLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectionLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConnectionLimitExceededException":
        return cls(deserialize_json(data))
