"""Generated from Smithy shape ``com.amazonaws.qbusiness#CancelSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.subscription_id


class CancelSubscriptionRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application for which the subscription is being cancelled.</p>"""
    subscription_id: "aws_sdk_qbusiness.types.subscription_id.SubscriptionId"
    """<p>The identifier of the Amazon Q Business subscription being cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSubscriptionRequest:
    out: CancelSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
