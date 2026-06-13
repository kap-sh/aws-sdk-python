"""Generated from Smithy shape ``com.amazonaws.quicksight#ListOAuthClientApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.string


class ListOAuthClientApplicationsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOAuthClientApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOAuthClientApplicationsRequest:
    out: ListOAuthClientApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
