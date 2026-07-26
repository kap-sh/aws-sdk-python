"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteSubscriptionGrantInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.subscription_grant_id


class DeleteSubscriptionGrantInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where the subscription grant is deleted.</p>"""
    identifier: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The ID of the subscription grant that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionGrantInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionGrantInput:
    out: DeleteSubscriptionGrantInput = {}  # type: ignore[typeddict-item]
    return out
