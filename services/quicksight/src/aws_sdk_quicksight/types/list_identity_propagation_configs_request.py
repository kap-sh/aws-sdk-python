"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIdentityPropagationConfigsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.list_identity_propagation_max_results
    import aws_sdk_quicksight.types.string


class ListIdentityPropagationConfigsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contain the identity propagation configurations of.</p>"""
    max_results: NotRequired[
        "aws_sdk_quicksight.types.list_identity_propagation_max_results.ListIdentityPropagationMaxResults"
    ]
    """<p>The maximum number of results to be returned.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityPropagationConfigsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentityPropagationConfigsRequest:
    out: ListIdentityPropagationConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
