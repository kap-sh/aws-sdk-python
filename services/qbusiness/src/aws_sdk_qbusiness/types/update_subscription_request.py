"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.subscription_id
    import aws_sdk_qbusiness.types.subscription_type


class UpdateSubscriptionRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application where the subscription update should take effect.</p>"""
    subscription_id: "aws_sdk_qbusiness.types.subscription_id.SubscriptionId"
    """<p>The identifier of the Amazon Q Business subscription to be updated.</p>"""
    type: "aws_sdk_qbusiness.types.subscription_type.SubscriptionType"
    """<p>The type of the Amazon Q Business subscription to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionRequest) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.subscription_type

    out["type"] = aws_sdk_qbusiness.types.subscription_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionRequest:
    out: UpdateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_qbusiness.types.subscription_type

        out["type"] = aws_sdk_qbusiness.types.subscription_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("UpdateSubscriptionRequest.type required")
    return out
