"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionRequestDetailsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_request_id


class GetSubscriptionRequestDetailsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to get the subscription request details.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The identifier of the subscription request the details of which to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionRequestDetailsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionRequestDetailsInput:
    out: GetSubscriptionRequestDetailsInput = {}  # type: ignore[typeddict-item]
    return out
