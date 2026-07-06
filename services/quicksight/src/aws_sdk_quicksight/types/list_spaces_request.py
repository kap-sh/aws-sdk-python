"""Generated from Smithy shape ``com.amazonaws.quicksight#ListSpacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.next_token
    import aws_sdk_quicksight.types.spaces_max_results


class ListSpacesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the spaces.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired[
        "aws_sdk_quicksight.types.spaces_max_results.SpacesMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSpacesRequest:
    out: ListSpacesRequest = {}  # type: ignore[typeddict-item]
    return out
