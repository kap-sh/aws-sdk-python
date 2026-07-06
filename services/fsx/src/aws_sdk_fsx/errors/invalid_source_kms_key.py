"""Generated from Smithy shape ``com.amazonaws.fsx#InvalidSourceKmsKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class InvalidSourceKmsKey_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSourceKmsKey_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSourceKmsKey_:
    out: InvalidSourceKmsKey_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidSourceKmsKey(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#InvalidSourceKmsKey``."""

    code: str | None = "InvalidSourceKmsKey"

    def __init__(self, data: InvalidSourceKmsKey_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSourceKmsKey",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidSourceKmsKey":
        return cls(deserialize_aws_json_1_1(data))
