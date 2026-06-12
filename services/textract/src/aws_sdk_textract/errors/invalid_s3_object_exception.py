"""Generated from Smithy shape ``com.amazonaws.textract#InvalidS3ObjectException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_textract.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_textract.types.string


class InvalidS3ObjectException_(TypedDict):
    message: NotRequired["aws_sdk_textract.types.string.String"]
    code: NotRequired["aws_sdk_textract.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidS3ObjectException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidS3ObjectException_:
    out: InvalidS3ObjectException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class InvalidS3ObjectException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.textract#InvalidS3ObjectException``."""

    code: str | None = "InvalidS3ObjectException"

    def __init__(self, data: InvalidS3ObjectException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3ObjectException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidS3ObjectException":
        return cls(deserialize_aws_json_1_1(data))
