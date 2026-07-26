"""Generated from Smithy shape ``com.amazonaws.textract#InternalServerError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import ServiceError

if TYPE_CHECKING:
    import capo_textract.types.string


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["capo_textract.types.string.String"]
    code: NotRequired["capo_textract.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.textract#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(self, data: InternalServerError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServerError":
        return cls(deserialize_aws_json_1_1(data))
