"""Generated from Smithy shape ``com.amazonaws.amplify#GetWebhookRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.webhook_id


class GetWebhookRequest(TypedDict, closed=True):
    webhook_id: "capo_amplify.types.webhook_id.WebhookId"
    """<p>The unique ID for a webhook. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebhookRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWebhookRequest:
    out: GetWebhookRequest = {}  # type: ignore[typeddict-item]
    return out
