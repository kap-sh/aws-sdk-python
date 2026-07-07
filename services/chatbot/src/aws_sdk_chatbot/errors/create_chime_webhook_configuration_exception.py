"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class CreateChimeWebhookConfigurationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateChimeWebhookConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateChimeWebhookConfigurationException_:
    out: CreateChimeWebhookConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CreateChimeWebhookConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationException``."""

    code: str | None = "CreateChimeWebhookConfigurationException"

    def __init__(self, data: CreateChimeWebhookConfigurationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="CreateChimeWebhookConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CreateChimeWebhookConfigurationException":
        return cls(deserialize_json(data))
