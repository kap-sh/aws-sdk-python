"""Generated from Smithy shape ``com.amazonaws.rekognition#ImageTooLargeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import ServiceError

if TYPE_CHECKING:
    import capo_rekognition.types.string


class ImageTooLargeException_(TypedDict, closed=True):
    message: NotRequired["capo_rekognition.types.string.String"]
    code: NotRequired["capo_rekognition.types.string.String"]
    logref: NotRequired["capo_rekognition.types.string.String"]
    """<p>A universally unique identifier (UUID) for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTooLargeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "logref" in value:
        out["Logref"] = value["logref"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageTooLargeException_:
    out: ImageTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Logref" in data:
        out["logref"] = data["Logref"]
    return out


class ImageTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rekognition#ImageTooLargeException``."""

    code: str | None = "ImageTooLargeException"

    def __init__(self, data: ImageTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImageTooLargeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ImageTooLargeException":
        return cls(deserialize_aws_json_1_1(data))
