"""Generated from Smithy shape ``com.amazonaws.textract#UnsupportedDocumentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import ServiceError

if TYPE_CHECKING:
    import capo_textract.types.string


class UnsupportedDocumentException_(TypedDict, closed=True):
    message: NotRequired["capo_textract.types.string.String"]
    code: NotRequired["capo_textract.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedDocumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedDocumentException_:
    out: UnsupportedDocumentException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class UnsupportedDocumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.textract#UnsupportedDocumentException``."""

    code: str | None = "UnsupportedDocumentException"

    def __init__(self, data: UnsupportedDocumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedDocumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedDocumentException":
        return cls(deserialize_aws_json_1_1(data))
