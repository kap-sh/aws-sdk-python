"""Generated from Smithy shape ``com.amazonaws.shield#InvalidPaginationTokenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_shield.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_shield.types.error_message


class InvalidPaginationTokenException_(TypedDict):
    message: NotRequired["aws_sdk_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPaginationTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPaginationTokenException_:
    out: InvalidPaginationTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidPaginationTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidPaginationTokenException``."""

    code: str | None = "InvalidPaginationTokenException"

    def __init__(self, data: InvalidPaginationTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationTokenException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPaginationTokenException":
        return cls(deserialize_aws_json_1_1(data))
