"""Generated from Smithy shape ``com.amazonaws.quicksight#ListGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.namespace
    import capo_quicksight.types.string


class ListGroupsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want a list of groups from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroupsRequest:
    out: ListGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
