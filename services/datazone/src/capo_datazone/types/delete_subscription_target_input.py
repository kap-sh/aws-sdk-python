"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteSubscriptionTargetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.subscription_target_id


class DeleteSubscriptionTargetInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription target is deleted.</p>"""
    environment_identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the Amazon DataZone environment in which the subscription target is deleted.</p>"""
    identifier: "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The ID of the subscription target that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionTargetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionTargetInput:
    out: DeleteSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
    return out
