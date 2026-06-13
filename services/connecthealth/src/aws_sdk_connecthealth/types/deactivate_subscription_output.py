"""Generated from Smithy shape ``com.amazonaws.connecthealth#DeactivateSubscriptionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.subscription_description


class DeactivateSubscriptionOutput(TypedDict):
    subscription: NotRequired[
        "aws_sdk_connecthealth.types.subscription_description.SubscriptionDescription"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeactivateSubscriptionOutput) -> dict:
    out: dict = {}
    if "subscription" in value:
        import aws_sdk_connecthealth.types.subscription_description

        out["subscription"] = (
            aws_sdk_connecthealth.types.subscription_description.serialize_json(
                value["subscription"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeactivateSubscriptionOutput:
    out: DeactivateSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if "subscription" in data:
        import aws_sdk_connecthealth.types.subscription_description

        out["subscription"] = (
            aws_sdk_connecthealth.types.subscription_description.deserialize_json(
                data["subscription"]
            )
        )
    return out
