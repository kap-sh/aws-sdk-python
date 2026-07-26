"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateWebhookResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.webhook


class UpdateWebhookResult(TypedDict, closed=True):
    webhook: "capo_amplify.types.webhook.Webhook"
    """<p>Describes a webhook that connects repository events to an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWebhookResult) -> dict:
    out: dict = {}
    import capo_amplify.types.webhook

    out["webhook"] = capo_amplify.types.webhook.serialize_json(value["webhook"])
    return out


def deserialize_json(data: dict) -> UpdateWebhookResult:
    out: UpdateWebhookResult = {}  # type: ignore[typeddict-item]
    if "webhook" in data:
        import capo_amplify.types.webhook

        out["webhook"] = capo_amplify.types.webhook.deserialize_json(data["webhook"])
    else:
        raise DeserializationError("UpdateWebhookResult.webhook required")
    return out
