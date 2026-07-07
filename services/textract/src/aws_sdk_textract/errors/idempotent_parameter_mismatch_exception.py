"""Generated from Smithy shape ``com.amazonaws.textract#IdempotentParameterMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_textract.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_textract.types.string


class IdempotentParameterMismatchException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_textract.types.string.String"]
    code: NotRequired["aws_sdk_textract.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdempotentParameterMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdempotentParameterMismatchException_:
    out: IdempotentParameterMismatchException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class IdempotentParameterMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.textract#IdempotentParameterMismatchException``."""

    code: str | None = "IdempotentParameterMismatchException"

    def __init__(self, data: IdempotentParameterMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentParameterMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IdempotentParameterMismatchException":
        return cls(deserialize_aws_json_1_1(data))
