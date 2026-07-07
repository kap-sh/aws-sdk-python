"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageTagAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.exception_message


class ImageTagAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageTagAlreadyExistsException_:
    out: ImageTagAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ImageTagAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#ImageTagAlreadyExistsException``."""

    code: str | None = "ImageTagAlreadyExistsException"

    def __init__(self, data: ImageTagAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImageTagAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ImageTagAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
