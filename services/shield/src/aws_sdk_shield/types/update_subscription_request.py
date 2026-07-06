"""Generated from Smithy shape ``com.amazonaws.shield#UpdateSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.auto_renew


class UpdateSubscriptionRequest(TypedDict, closed=True):
    auto_renew: NotRequired["aws_sdk_shield.types.auto_renew.AutoRenew"]
    """<p>When you initally create a subscription, <code>AutoRenew</code> is set to <code>ENABLED</code>. If <code>ENABLED</code>, the subscription will be automatically renewed at the end of the existing subscription period. You can change this by submitting an <code>UpdateSubscription</code> request. If the <code>UpdateSubscription</code> request does not included a value for <code>AutoRenew</code>, the existing value for <code>AutoRenew</code> remains unchanged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubscriptionRequest) -> dict:
    out: dict = {}
    if "auto_renew" in value:
        import aws_sdk_shield.types.auto_renew

        out["AutoRenew"] = aws_sdk_shield.types.auto_renew.serialize_aws_json_1_1(
            value["auto_renew"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubscriptionRequest:
    out: UpdateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "AutoRenew" in data:
        import aws_sdk_shield.types.auto_renew

        out["auto_renew"] = aws_sdk_shield.types.auto_renew.deserialize_aws_json_1_1(
            data["AutoRenew"]
        )
    return out
