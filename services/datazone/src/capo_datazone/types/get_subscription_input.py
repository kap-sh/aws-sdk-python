"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.subscription_id


class GetSubscriptionInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription exists.</p>"""
    identifier: "capo_datazone.types.subscription_id.SubscriptionId"
    """<p>The ID of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionInput:
    out: GetSubscriptionInput = {}  # type: ignore[typeddict-item]
    return out
