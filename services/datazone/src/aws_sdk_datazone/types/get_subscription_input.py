"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_id


class GetSubscriptionInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription exists.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    """<p>The ID of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionInput:
    out: GetSubscriptionInput = {}  # type: ignore[typeddict-item]
    return out
