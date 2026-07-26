"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeregisterWebhookWithThirdPartyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.webhook_name


class DeregisterWebhookWithThirdPartyInput(TypedDict, closed=True):
    webhook_name: NotRequired["capo_codepipeline.types.webhook_name.WebhookName"]
    """<p>The name of the webhook you want to deregister.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterWebhookWithThirdPartyInput) -> dict:
    out: dict = {}
    if "webhook_name" in value:
        out["webhookName"] = value["webhook_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterWebhookWithThirdPartyInput:
    out: DeregisterWebhookWithThirdPartyInput = {}  # type: ignore[typeddict-item]
    if "webhookName" in data:
        out["webhook_name"] = data["webhookName"]
    return out
