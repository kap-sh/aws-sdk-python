"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidDocumentType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidDocumentType_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDocumentType_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDocumentType_:
    out: InvalidDocumentType_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidDocumentType(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidDocumentType``."""

    code: str | None = "InvalidDocumentType"

    def __init__(self, data: InvalidDocumentType_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDocumentType",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidDocumentType":
        return cls(deserialize_aws_json_1_1(data))
