"""Generated from Smithy shape ``com.amazonaws.chatbot#GetAccountPreferencesException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class GetAccountPreferencesException_(TypedDict):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountPreferencesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetAccountPreferencesException_:
    out: GetAccountPreferencesException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class GetAccountPreferencesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#GetAccountPreferencesException``."""

    code: str | None = "GetAccountPreferencesException"

    def __init__(self, data: GetAccountPreferencesException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="GetAccountPreferencesException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "GetAccountPreferencesException":
        return cls(deserialize_json(data))
