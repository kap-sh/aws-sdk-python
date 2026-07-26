"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFolderPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.namespace
    import capo_quicksight.types.restrictive_resource_id
    import capo_quicksight.types.string


class DescribeFolderPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder.</p>"""
    folder_id: "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The namespace of the folder whose permissions you want described.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFolderPermissionsRequest:
    out: DescribeFolderPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
