"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateChimeWebhookConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chime_webhook_configuration


class CreateChimeWebhookConfigurationResult(TypedDict, closed=True):
    webhook_configuration: NotRequired[
        "aws_sdk_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration"
    ]
    """<p>An Amazon Chime webhook configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChimeWebhookConfigurationResult) -> dict:
    out: dict = {}
    if "webhook_configuration" in value:
        import aws_sdk_chatbot.types.chime_webhook_configuration

        out["WebhookConfiguration"] = (
            aws_sdk_chatbot.types.chime_webhook_configuration.serialize_json(
                value["webhook_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateChimeWebhookConfigurationResult:
    out: CreateChimeWebhookConfigurationResult = {}  # type: ignore[typeddict-item]
    if "WebhookConfiguration" in data:
        import aws_sdk_chatbot.types.chime_webhook_configuration

        out["webhook_configuration"] = (
            aws_sdk_chatbot.types.chime_webhook_configuration.deserialize_json(
                data["WebhookConfiguration"]
            )
        )
    return out
