"""Generated from Smithy shape ``com.amazonaws.devopsagent#GenericWebhook``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.api_key_value
    import aws_sdk_devops_agent.types.webhook_secret
    import aws_sdk_devops_agent.types.webhook_type


class GenericWebhook(TypedDict):
    webhook_url: NotRequired["str"]
    """<p>The webhook URL endpoint</p>"""
    webhook_id: NotRequired["str"]
    """<p>The unique webhook identifier</p>"""
    webhook_type: NotRequired["aws_sdk_devops_agent.types.webhook_type.WebhookType"]
    """<p>The webhook authentication type</p>"""
    webhook_secret: NotRequired[
        "aws_sdk_devops_agent.types.webhook_secret.WebhookSecret"
    ]
    """<p>The webhook secret for authentication</p>"""
    api_key: NotRequired["aws_sdk_devops_agent.types.api_key_value.ApiKeyValue"]
    """<p>API Key for API Key webhook authentication</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenericWebhook) -> dict:
    out: dict = {}
    if "webhook_url" in value:
        out["webhookUrl"] = value["webhook_url"]
    if "webhook_id" in value:
        out["webhookId"] = value["webhook_id"]
    if "webhook_type" in value:
        import aws_sdk_devops_agent.types.webhook_type

        out["webhookType"] = aws_sdk_devops_agent.types.webhook_type.serialize_json(
            value["webhook_type"]
        )
    if "webhook_secret" in value:
        out["webhookSecret"] = value["webhook_secret"]
    if "api_key" in value:
        out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> GenericWebhook:
    out: GenericWebhook = {}  # type: ignore[typeddict-item]
    if "webhookUrl" in data:
        out["webhook_url"] = data["webhookUrl"]
    if "webhookId" in data:
        out["webhook_id"] = data["webhookId"]
    if "webhookType" in data:
        import aws_sdk_devops_agent.types.webhook_type

        out["webhook_type"] = aws_sdk_devops_agent.types.webhook_type.deserialize_json(
            data["webhookType"]
        )
    if "webhookSecret" in data:
        out["webhook_secret"] = data["webhookSecret"]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    return out
