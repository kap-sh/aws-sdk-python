"""Generated from Smithy shape ``com.amazonaws.ecr#ImageArchivedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class ImageArchivedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageArchivedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageArchivedException_:
    out: ImageArchivedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ImageArchivedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#ImageArchivedException``."""

    code: str | None = "ImageArchivedException"

    def __init__(self, data: ImageArchivedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImageArchivedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ImageArchivedException":
        return cls(deserialize_aws_json_1_1(data))
