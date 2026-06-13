"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.asset_bundle_import_failure_action
    import aws_sdk_quicksight.types.asset_bundle_import_job_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.timestamp


class AssetBundleImportJobSummary(TypedDict):
    job_status: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_status.AssetBundleImportJobStatus"
    ]
    """<p>The current status of the import job.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the import job.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the import job was created.</p>"""
    asset_bundle_import_job_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.</p>"""
    failure_action: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_failure_action.AssetBundleImportFailureAction"
    ]
    """<p>The failure action for the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobSummary) -> dict:
    out: dict = {}
    if "job_status" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_status

        out["JobStatus"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_status.serialize_json(
                value["job_status"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "asset_bundle_import_job_id" in value:
        out["AssetBundleImportJobId"] = value["asset_bundle_import_job_id"]
    if "failure_action" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_failure_action

        out["FailureAction"] = (
            aws_sdk_quicksight.types.asset_bundle_import_failure_action.serialize_json(
                value["failure_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobSummary:
    out: AssetBundleImportJobSummary = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_status

        out["job_status"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "AssetBundleImportJobId" in data:
        out["asset_bundle_import_job_id"] = data["AssetBundleImportJobId"]
    if "FailureAction" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_failure_action

        out["failure_action"] = (
            aws_sdk_quicksight.types.asset_bundle_import_failure_action.deserialize_json(
                data["FailureAction"]
            )
        )
    return out
