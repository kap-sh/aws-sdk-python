"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteSubscriptionRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_request_id


class DeleteSubscriptionRequestInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription request is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The ID of the subscription request that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionRequestInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionRequestInput:
    out: DeleteSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    return out
