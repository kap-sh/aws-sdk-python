"""Generated from Smithy shape ``com.amazonaws.devopsagent#WebhookType``."""

from typing import Literal, TypeAlias, cast

"""<p>Webhook authentication type.</p>"""
WebhookType: TypeAlias = Literal[
    "hmac",
    "apikey",
    "gitlab",
    "pagerduty",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebhookType) -> str:
    return value


def deserialize_json(data: str) -> WebhookType:
    return cast(WebhookType, data)
