"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoTooLargeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string


class VideoTooLargeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rekognition.types.string.String"]
    code: NotRequired["aws_sdk_rekognition.types.string.String"]
    logref: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>A universally unique identifier (UUID) for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoTooLargeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "logref" in value:
        out["Logref"] = value["logref"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VideoTooLargeException_:
    out: VideoTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Logref" in data:
        out["logref"] = data["Logref"]
    return out


class VideoTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rekognition#VideoTooLargeException``."""

    code: str | None = "VideoTooLargeException"

    def __init__(self, data: VideoTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VideoTooLargeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "VideoTooLargeException":
        return cls(deserialize_aws_json_1_1(data))
