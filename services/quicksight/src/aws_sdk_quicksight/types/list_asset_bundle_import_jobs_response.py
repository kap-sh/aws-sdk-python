"""Generated from Smithy shape ``com.amazonaws.quicksight#ListAssetBundleImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_summary_list
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListAssetBundleImportJobsResponse(TypedDict):
    asset_bundle_import_job_summary_list: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_summary_list.AssetBundleImportJobSummaryList"
    ]
    """<p>A list of import job summaries.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetBundleImportJobsResponse) -> dict:
    out: dict = {}
    if "asset_bundle_import_job_summary_list" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_summary_list

        out["AssetBundleImportJobSummaryList"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_summary_list.serialize_json(
                value["asset_bundle_import_job_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListAssetBundleImportJobsResponse:
    out: ListAssetBundleImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "AssetBundleImportJobSummaryList" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_summary_list

        out["asset_bundle_import_job_summary_list"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_summary_list.deserialize_json(
                data["AssetBundleImportJobSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
