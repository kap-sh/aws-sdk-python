"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.exception_message


class ImageAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageAlreadyExistsException_:
    out: ImageAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ImageAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#ImageAlreadyExistsException``."""

    code: str | None = "ImageAlreadyExistsException"

    def __init__(self, data: ImageAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImageAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ImageAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
