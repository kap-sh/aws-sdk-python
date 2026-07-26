"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListSubscriptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.subscription_list


class ListSubscriptionsOutput(TypedDict, closed=True):
    subscriptions: "capo_connecthealth.types.subscription_list.SubscriptionList"
    """<p>List of Subscriptions.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsOutput) -> dict:
    out: dict = {}
    import capo_connecthealth.types.subscription_list

    out["subscriptions"] = capo_connecthealth.types.subscription_list.serialize_json(
        value["subscriptions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionsOutput:
    out: ListSubscriptionsOutput = {}  # type: ignore[typeddict-item]
    if "subscriptions" in data:
        import capo_connecthealth.types.subscription_list

        out["subscriptions"] = (
            capo_connecthealth.types.subscription_list.deserialize_json(
                data["subscriptions"]
            )
        )
    else:
        raise DeserializationError("ListSubscriptionsOutput.subscriptions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
