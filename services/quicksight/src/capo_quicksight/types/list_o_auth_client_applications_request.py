"""Generated from Smithy shape ``com.amazonaws.quicksight#ListOAuthClientApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.string


class ListOAuthClientApplicationsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOAuthClientApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOAuthClientApplicationsRequest:
    out: ListOAuthClientApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
