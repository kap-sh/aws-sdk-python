"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.pagination_token
    import capo_datazone.types.subscriptions


class ListSubscriptionsOutput(TypedDict, closed=True):
    items: "capo_datazone.types.subscriptions.Subscriptions"
    """<p>The results of the <code>ListSubscriptions</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscriptions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscriptions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptions</code> to list the next set of subscriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.subscriptions

    out["items"] = capo_datazone.types.subscriptions.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionsOutput:
    out: ListSubscriptionsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_datazone.types.subscriptions

        out["items"] = capo_datazone.types.subscriptions.deserialize_json(data["items"])
    else:
        raise DeserializationError("ListSubscriptionsOutput.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
