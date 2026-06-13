"""Generated from Smithy shape ``com.amazonaws.datazone#CancelSubscriptionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_id


class CancelSubscriptionInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The unique identifier of the Amazon DataZone domain where the subscription request is being cancelled.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    """<p>The unique identifier of the subscription that is being cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSubscriptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSubscriptionInput:
    out: CancelSubscriptionInput = {}  # type: ignore[typeddict-item]
    return out
