"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StreamEdgeConfigurationNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.error_message


class StreamEdgeConfigurationNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis_video.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamEdgeConfigurationNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StreamEdgeConfigurationNotFoundException_:
    out: StreamEdgeConfigurationNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class StreamEdgeConfigurationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideo#StreamEdgeConfigurationNotFoundException``."""

    code: str | None = "StreamEdgeConfigurationNotFoundException"

    def __init__(self, data: StreamEdgeConfigurationNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StreamEdgeConfigurationNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "StreamEdgeConfigurationNotFoundException":
        return cls(deserialize_json(data))
