"""Generated from Smithy shape ``com.amazonaws.sns#ListSubscriptionsByTopicResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.next_token
    import aws_sdk_sns.types.subscriptions_list


class ListSubscriptionsByTopicResponse(TypedDict):
    subscriptions: NotRequired["aws_sdk_sns.types.subscriptions_list.SubscriptionsList"]
    """<p>A list of subscriptions.</p>"""
    next_token: NotRequired["aws_sdk_sns.types.next_token.nextToken"]
    """<p>Token to pass along to the next <code>ListSubscriptionsByTopic</code> request. This element is returned if there are more subscriptions to retrieve.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSubscriptionsByTopicResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subscriptions" in value:
        import aws_sdk_sns.types.subscriptions_list

        aws_sdk_sns.types.subscriptions_list.serialize_query(
            value["subscriptions"], pairs, f"{prefix}.Subscriptions"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListSubscriptionsByTopicResponse:
    out: ListSubscriptionsByTopicResponse = {}  # type: ignore[typeddict-item]
    child_subscriptions = el.find("Subscriptions")
    if child_subscriptions is not None:
        import aws_sdk_sns.types.subscriptions_list

        out["subscriptions"] = aws_sdk_sns.types.subscriptions_list.deserialize_query(
            child_subscriptions
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
