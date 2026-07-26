"""Generated from Smithy shape ``com.amazonaws.connecthealth#ActivateSubscriptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.subscription_description


class ActivateSubscriptionOutput(TypedDict, closed=True):
    subscription: NotRequired[
        "capo_connecthealth.types.subscription_description.SubscriptionDescription"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateSubscriptionOutput) -> dict:
    out: dict = {}
    if "subscription" in value:
        import capo_connecthealth.types.subscription_description

        out["subscription"] = (
            capo_connecthealth.types.subscription_description.serialize_json(
                value["subscription"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActivateSubscriptionOutput:
    out: ActivateSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if "subscription" in data:
        import capo_connecthealth.types.subscription_description

        out["subscription"] = (
            capo_connecthealth.types.subscription_description.deserialize_json(
                data["subscription"]
            )
        )
    return out
