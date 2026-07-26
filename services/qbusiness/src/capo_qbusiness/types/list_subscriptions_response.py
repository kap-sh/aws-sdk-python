"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListSubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.subscriptions


class ListSubscriptionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token. You can use this token in a subsequent request to retrieve the next set of subscriptions.</p>"""
    subscriptions: NotRequired["capo_qbusiness.types.subscriptions.Subscriptions"]
    """<p>An array of summary information on the subscriptions configured for an Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "subscriptions" in value:
        import capo_qbusiness.types.subscriptions

        out["subscriptions"] = capo_qbusiness.types.subscriptions.serialize_json(
            value["subscriptions"]
        )
    return out


def deserialize_json(data: dict) -> ListSubscriptionsResponse:
    out: ListSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "subscriptions" in data:
        import capo_qbusiness.types.subscriptions

        out["subscriptions"] = capo_qbusiness.types.subscriptions.deserialize_json(
            data["subscriptions"]
        )
    return out
