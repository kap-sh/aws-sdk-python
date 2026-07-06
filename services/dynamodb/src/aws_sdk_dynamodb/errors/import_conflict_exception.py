"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ImportConflictException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportConflictException_:
    out: ImportConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ImportConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ImportConflictException``."""

    code: str | None = "ImportConflictException"

    def __init__(self, data: ImportConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImportConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ImportConflictException":
        return cls(deserialize_aws_json_1_0(data))
