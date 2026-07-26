"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAssetBundleExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DescribeAssetBundleExportJobRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account the export job is executed in. </p>"""
    asset_bundle_export_job_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the job that you want described. The job ID is set when you start a new job with a <code>StartAssetBundleExportJob</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetBundleExportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetBundleExportJobRequest:
    out: DescribeAssetBundleExportJobRequest = {}  # type: ignore[typeddict-item]
    return out
