"""Generated from Smithy shape ``com.amazonaws.devopsagent#WebhookType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Webhook authentication type.</p>"""
WebhookType: TypeAlias = Literal[
    "hmac",
    "apikey",
    "gitlab",
    "pagerduty",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "hmac",
        "apikey",
        "gitlab",
        "pagerduty",
    )
)


def serialize_json(value: WebhookType) -> str:
    return value


def deserialize_json(data: str) -> WebhookType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebhookType value: {data!r}")
    return cast(WebhookType, data)
