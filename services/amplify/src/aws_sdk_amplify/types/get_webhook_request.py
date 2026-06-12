"""Generated from Smithy shape ``com.amazonaws.amplify#GetWebhookRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.webhook_id


class GetWebhookRequest(TypedDict):
    webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId"
    """<p>The unique ID for a webhook. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebhookRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWebhookRequest:
    out: GetWebhookRequest = {}  # type: ignore[typeddict-item]
    return out
