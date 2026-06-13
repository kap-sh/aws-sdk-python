"""Generated from Smithy shape ``com.amazonaws.devopsagent#WebhooksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.webhook

WebhooksList: TypeAlias = list["aws_sdk_devops_agent.types.webhook.Webhook"]


# --- restJson1 ser/de ---
def serialize_json(value: WebhooksList) -> list:
    import aws_sdk_devops_agent.types.webhook

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.webhook.serialize_json(item))
    return out


def deserialize_json(data: list) -> WebhooksList:
    import aws_sdk_devops_agent.types.webhook

    out: WebhooksList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.webhook.deserialize_json(item))
    return out
