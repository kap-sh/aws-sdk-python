"""Generated from Smithy shape ``com.amazonaws.kms#InvalidImportTokenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class InvalidImportTokenException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidImportTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidImportTokenException_:
    out: InvalidImportTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidImportTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidImportTokenException``."""

    code: str | None = "InvalidImportTokenException"

    def __init__(self, data: InvalidImportTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidImportTokenException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidImportTokenException":
        return cls(deserialize_aws_json_1_1(data))
