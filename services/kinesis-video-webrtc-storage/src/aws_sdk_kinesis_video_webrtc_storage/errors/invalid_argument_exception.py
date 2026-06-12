"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#InvalidArgumentException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_webrtc_storage.errors import ServiceError


class InvalidArgumentException_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidArgumentException_:
    out: InvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#InvalidArgumentException``."""

    code: str | None = "InvalidArgumentException"

    def __init__(self, data: InvalidArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArgumentException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidArgumentException":
        return cls(deserialize_json(data))
