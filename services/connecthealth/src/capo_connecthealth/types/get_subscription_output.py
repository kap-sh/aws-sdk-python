"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetSubscriptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.subscription_description


class GetSubscriptionOutput(TypedDict, closed=True):
    subscription: NotRequired[
        "capo_connecthealth.types.subscription_description.SubscriptionDescription"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionOutput) -> dict:
    out: dict = {}
    if "subscription" in value:
        import capo_connecthealth.types.subscription_description

        out["subscription"] = (
            capo_connecthealth.types.subscription_description.serialize_json(
                value["subscription"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSubscriptionOutput:
    out: GetSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if "subscription" in data:
        import capo_connecthealth.types.subscription_description

        out["subscription"] = (
            capo_connecthealth.types.subscription_description.deserialize_json(
                data["subscription"]
            )
        )
    return out
