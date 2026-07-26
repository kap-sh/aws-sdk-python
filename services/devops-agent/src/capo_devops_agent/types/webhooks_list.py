"""Generated from Smithy shape ``com.amazonaws.devopsagent#WebhooksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.webhook

WebhooksList: TypeAlias = list["capo_devops_agent.types.webhook.Webhook"]


# --- restJson1 ser/de ---
def serialize_json(value: WebhooksList) -> list:
    import capo_devops_agent.types.webhook

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.webhook.serialize_json(item))
    return out


def deserialize_json(data: list) -> WebhooksList:
    import capo_devops_agent.types.webhook

    out: WebhooksList = []
    for item in data:
        out.append(capo_devops_agent.types.webhook.deserialize_json(item))
    return out
