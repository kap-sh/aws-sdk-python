"""Generated from Smithy shape ``com.amazonaws.quicksight#ListBrandsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.string


class ListBrandsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brands that you want to list.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned in a single request.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrandsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBrandsRequest:
    out: ListBrandsRequest = {}  # type: ignore[typeddict-item]
    return out
