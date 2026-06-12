"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class S3AccessPointAttachmentNotFound_(TypedDict):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3AccessPointAttachmentNotFound_:
    out: S3AccessPointAttachmentNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class S3AccessPointAttachmentNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentNotFound``."""

    code: str | None = "S3AccessPointAttachmentNotFound"

    def __init__(self, data: S3AccessPointAttachmentNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="S3AccessPointAttachmentNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "S3AccessPointAttachmentNotFound":
        return cls(deserialize_aws_json_1_1(data))
