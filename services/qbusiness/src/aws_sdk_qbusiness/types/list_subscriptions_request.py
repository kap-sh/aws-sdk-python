"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListSubscriptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_subscriptions
    import aws_sdk_qbusiness.types.next_token


class ListSubscriptionsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to the subscription.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business subscriptions.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_subscriptions.MaxResultsIntegerForListSubscriptions"
    ]
    """<p>The maximum number of Amazon Q Business subscriptions to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionsRequest:
    out: ListSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    return out
