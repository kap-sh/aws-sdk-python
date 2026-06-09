"""Generated from Smithy shape ``com.amazonaws.dynamodb#InvalidExportTimeException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class InvalidExportTimeException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidExportTimeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidExportTimeException_:
    out: InvalidExportTimeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidExportTimeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#InvalidExportTimeException``."""

    code: str | None = "InvalidExportTimeException"

    def __init__(self, data: InvalidExportTimeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExportTimeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidExportTimeException":
        return cls(deserialize_aws_json_1_0(data))
