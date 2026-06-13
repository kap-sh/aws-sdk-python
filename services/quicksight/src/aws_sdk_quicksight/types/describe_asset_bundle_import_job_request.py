"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAssetBundleImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeAssetBundleImportJobRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account the import job was executed in. </p>"""
    asset_bundle_import_job_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the job. The job ID is set when you start a new job with a <code>StartAssetBundleImportJob</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetBundleImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetBundleImportJobRequest:
    out: DescribeAssetBundleImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
