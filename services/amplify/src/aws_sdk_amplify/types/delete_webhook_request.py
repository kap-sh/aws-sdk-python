"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteWebhookRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.webhook_id


class DeleteWebhookRequest(TypedDict):
    webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId"
    """<p>The unique ID for a webhook. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWebhookRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWebhookRequest:
    out: DeleteWebhookRequest = {}  # type: ignore[typeddict-item]
    return out
