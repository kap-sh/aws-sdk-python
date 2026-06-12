"""Generated from Smithy shape ``com.amazonaws.shield#DescribeSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.subscription


class DescribeSubscriptionResponse(TypedDict):
    subscription: NotRequired["aws_sdk_shield.types.subscription.Subscription"]
    """<p>The Shield Advanced subscription details for an account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import aws_sdk_shield.types.subscription

        out["Subscription"] = aws_sdk_shield.types.subscription.serialize_aws_json_1_1(
            value["subscription"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscriptionResponse:
    out: DescribeSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "Subscription" in data:
        import aws_sdk_shield.types.subscription

        out["subscription"] = (
            aws_sdk_shield.types.subscription.deserialize_aws_json_1_1(
                data["Subscription"]
            )
        )
    return out
