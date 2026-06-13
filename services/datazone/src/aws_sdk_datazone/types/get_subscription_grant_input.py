"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionGrantInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_grant_id


class GetSubscriptionGrantInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription grant exists.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The ID of the subscription grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionGrantInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionGrantInput:
    out: GetSubscriptionGrantInput = {}  # type: ignore[typeddict-item]
    return out
