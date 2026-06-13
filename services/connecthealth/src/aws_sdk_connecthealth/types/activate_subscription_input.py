"""Generated from Smithy shape ``com.amazonaws.connecthealth#ActivateSubscriptionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.subscription_id


class ActivateSubscriptionInput(TypedDict):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId"
    """<p>The unique identifier of the Subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateSubscriptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ActivateSubscriptionInput:
    out: ActivateSubscriptionInput = {}  # type: ignore[typeddict-item]
    return out
