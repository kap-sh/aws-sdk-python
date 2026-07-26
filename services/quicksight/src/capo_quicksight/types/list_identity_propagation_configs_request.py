"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIdentityPropagationConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.list_identity_propagation_max_results
    import capo_quicksight.types.string


class ListIdentityPropagationConfigsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contain the identity propagation configurations of.</p>"""
    max_results: NotRequired[
        "capo_quicksight.types.list_identity_propagation_max_results.ListIdentityPropagationMaxResults"
    ]
    """<p>The maximum number of results to be returned.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityPropagationConfigsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentityPropagationConfigsRequest:
    out: ListIdentityPropagationConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
