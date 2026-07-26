"""Generated from Smithy shape ``com.amazonaws.connecthealth#DeactivateSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.subscription_id


class DeactivateSubscriptionInput(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId"
    """<p>The unique identifier of the Subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeactivateSubscriptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeactivateSubscriptionInput:
    out: DeactivateSubscriptionInput = {}  # type: ignore[typeddict-item]
    return out
