"""Generated from Smithy shape ``com.amazonaws.amplify#Webhooks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.webhook

Webhooks: TypeAlias = list["capo_amplify.types.webhook.Webhook"]


# --- restJson1 ser/de ---
def serialize_json(value: Webhooks) -> list:
    import capo_amplify.types.webhook

    out: list = []
    for item in value:
        out.append(capo_amplify.types.webhook.serialize_json(item))
    return out


def deserialize_json(data: list) -> Webhooks:
    import capo_amplify.types.webhook

    out: Webhooks = []
    for item in data:
        out.append(capo_amplify.types.webhook.deserialize_json(item))
    return out
