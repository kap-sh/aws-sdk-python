"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAssetBundleExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code


class StartAssetBundleExportJobResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the export job.</p>"""
    asset_bundle_export_job_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services response ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssetBundleExportJobResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "asset_bundle_export_job_id" in value:
        out["AssetBundleExportJobId"] = value["asset_bundle_export_job_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> StartAssetBundleExportJobResponse:
    out: StartAssetBundleExportJobResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AssetBundleExportJobId" in data:
        out["asset_bundle_export_job_id"] = data["AssetBundleExportJobId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
