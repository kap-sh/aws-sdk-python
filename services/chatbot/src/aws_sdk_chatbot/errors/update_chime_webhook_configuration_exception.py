"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateChimeWebhookConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class UpdateChimeWebhookConfigurationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChimeWebhookConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateChimeWebhookConfigurationException_:
    out: UpdateChimeWebhookConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UpdateChimeWebhookConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#UpdateChimeWebhookConfigurationException``."""

    code: str | None = "UpdateChimeWebhookConfigurationException"

    def __init__(self, data: UpdateChimeWebhookConfigurationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="UpdateChimeWebhookConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UpdateChimeWebhookConfigurationException":
        return cls(deserialize_json(data))
