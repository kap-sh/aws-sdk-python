"""Generated from Smithy shape ``com.amazonaws.devopsagent#Webhook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.webhook_type


class Webhook(TypedDict, closed=True):
    webhook_url: "str"
    """<p>Webhook endpoint URL.</p>"""
    webhook_type: NotRequired["aws_sdk_devops_agent.types.webhook_type.WebhookType"]
    """<p>Webhook authentication type.</p>"""
    webhook_id: "str"
    """<p>The unique identifier of the Webhook</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Webhook) -> dict:
    out: dict = {}
    out["webhookUrl"] = value["webhook_url"]
    if "webhook_type" in value:
        import aws_sdk_devops_agent.types.webhook_type

        out["webhookType"] = aws_sdk_devops_agent.types.webhook_type.serialize_json(
            value["webhook_type"]
        )
    out["webhookId"] = value["webhook_id"]
    return out


def deserialize_json(data: dict) -> Webhook:
    out: Webhook = {}  # type: ignore[typeddict-item]
    if "webhookUrl" in data:
        out["webhook_url"] = data["webhookUrl"]
    else:
        raise DeserializationError("Webhook.webhook_url required")
    if "webhookType" in data:
        import aws_sdk_devops_agent.types.webhook_type

        out["webhook_type"] = aws_sdk_devops_agent.types.webhook_type.deserialize_json(
            data["webhookType"]
        )
    if "webhookId" in data:
        out["webhook_id"] = data["webhookId"]
    else:
        raise DeserializationError("Webhook.webhook_id required")
    return out
