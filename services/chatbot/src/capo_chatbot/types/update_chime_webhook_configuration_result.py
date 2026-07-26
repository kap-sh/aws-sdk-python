"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateChimeWebhookConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chime_webhook_configuration


class UpdateChimeWebhookConfigurationResult(TypedDict, closed=True):
    webhook_configuration: NotRequired[
        "capo_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration"
    ]
    """<p>A Amazon Chime webhook configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChimeWebhookConfigurationResult) -> dict:
    out: dict = {}
    if "webhook_configuration" in value:
        import capo_chatbot.types.chime_webhook_configuration

        out["WebhookConfiguration"] = (
            capo_chatbot.types.chime_webhook_configuration.serialize_json(
                value["webhook_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChimeWebhookConfigurationResult:
    out: UpdateChimeWebhookConfigurationResult = {}  # type: ignore[typeddict-item]
    if "WebhookConfiguration" in data:
        import capo_chatbot.types.chime_webhook_configuration

        out["webhook_configuration"] = (
            capo_chatbot.types.chime_webhook_configuration.deserialize_json(
                data["WebhookConfiguration"]
            )
        )
    return out
