"""Generated from Smithy shape ``com.amazonaws.sns#ListSubscriptionsByTopicResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.next_token
    import capo_sns.types.subscriptions_list


class ListSubscriptionsByTopicResponse(TypedDict, closed=True):
    subscriptions: NotRequired["capo_sns.types.subscriptions_list.SubscriptionsList"]
    """<p>A list of subscriptions.</p>"""
    next_token: NotRequired["capo_sns.types.next_token.nextToken"]
    """<p>Token to pass along to the next <code>ListSubscriptionsByTopic</code> request. This element is returned if there are more subscriptions to retrieve.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSubscriptionsByTopicResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subscriptions" in value:
        import capo_sns.types.subscriptions_list

        capo_sns.types.subscriptions_list.serialize_query(
            value["subscriptions"], pairs, f"{key_prefix}Subscriptions"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListSubscriptionsByTopicResponse:
    out: ListSubscriptionsByTopicResponse = {}  # type: ignore[typeddict-item]
    child_subscriptions = el.find("Subscriptions")
    if child_subscriptions is not None:
        import capo_sns.types.subscriptions_list

        out["subscriptions"] = capo_sns.types.subscriptions_list.deserialize_query(
            child_subscriptions
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
