"""Generated from Smithy shape ``com.amazonaws.ecr#ReferencedImagesNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class ReferencedImagesNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferencedImagesNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferencedImagesNotFoundException_:
    out: ReferencedImagesNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ReferencedImagesNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#ReferencedImagesNotFoundException``."""

    code: str | None = "ReferencedImagesNotFoundException"

    def __init__(self, data: ReferencedImagesNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReferencedImagesNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ReferencedImagesNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
