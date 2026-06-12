"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#AccountChannelLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.error_message


class AccountChannelLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis_video.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountChannelLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccountChannelLimitExceededException_:
    out: AccountChannelLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccountChannelLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideo#AccountChannelLimitExceededException``."""

    code: str | None = "AccountChannelLimitExceededException"

    def __init__(self, data: AccountChannelLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountChannelLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccountChannelLimitExceededException":
        return cls(deserialize_json(data))
