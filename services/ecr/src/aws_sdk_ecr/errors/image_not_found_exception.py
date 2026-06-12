"""Generated from Smithy shape ``com.amazonaws.ecr#ImageNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class ImageNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageNotFoundException_:
    out: ImageNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ImageNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#ImageNotFoundException``."""

    code: str | None = "ImageNotFoundException"

    def __init__(self, data: ImageNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImageNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ImageNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
