"""Generated from Smithy shape ``com.amazonaws.qbusiness#SubscriptionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.subscription_type


class SubscriptionDetails(TypedDict):
    type: NotRequired["aws_sdk_qbusiness.types.subscription_type.SubscriptionType"]
    """<p> The type of an Amazon Q Business subscription. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionDetails) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_qbusiness.types.subscription_type

        out["type"] = aws_sdk_qbusiness.types.subscription_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> SubscriptionDetails:
    out: SubscriptionDetails = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_qbusiness.types.subscription_type

        out["type"] = aws_sdk_qbusiness.types.subscription_type.deserialize_json(
            data["type"]
        )
    return out
