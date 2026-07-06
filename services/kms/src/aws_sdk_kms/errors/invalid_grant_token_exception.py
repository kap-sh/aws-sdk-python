"""Generated from Smithy shape ``com.amazonaws.kms#InvalidGrantTokenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class InvalidGrantTokenException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidGrantTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidGrantTokenException_:
    out: InvalidGrantTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidGrantTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidGrantTokenException``."""

    code: str | None = "InvalidGrantTokenException"

    def __init__(self, data: InvalidGrantTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidGrantTokenException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidGrantTokenException":
        return cls(deserialize_aws_json_1_1(data))
