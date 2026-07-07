"""Generated from Smithy shape ``com.amazonaws.quicksight#ListAssetBundleImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.string


class ListAssetBundleImportJobsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that the import jobs were executed in.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetBundleImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetBundleImportJobsRequest:
    out: ListAssetBundleImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
