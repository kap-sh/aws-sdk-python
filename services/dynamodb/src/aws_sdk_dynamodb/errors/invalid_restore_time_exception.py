"""Generated from Smithy shape ``com.amazonaws.dynamodb#InvalidRestoreTimeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class InvalidRestoreTimeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidRestoreTimeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidRestoreTimeException_:
    out: InvalidRestoreTimeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidRestoreTimeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#InvalidRestoreTimeException``."""

    code: str | None = "InvalidRestoreTimeException"

    def __init__(self, data: InvalidRestoreTimeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRestoreTimeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidRestoreTimeException":
        return cls(deserialize_aws_json_1_0(data))
