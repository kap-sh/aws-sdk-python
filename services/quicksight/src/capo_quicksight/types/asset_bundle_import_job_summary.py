"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_bundle_import_failure_action
    import capo_quicksight.types.asset_bundle_import_job_status
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.timestamp


class AssetBundleImportJobSummary(TypedDict, closed=True):
    job_status: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_status.AssetBundleImportJobStatus"
    ]
    """<p>The current status of the import job.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the import job.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the import job was created.</p>"""
    asset_bundle_import_job_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.</p>"""
    failure_action: NotRequired[
        "capo_quicksight.types.asset_bundle_import_failure_action.AssetBundleImportFailureAction"
    ]
    """<p>The failure action for the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobSummary) -> dict:
    out: dict = {}
    if "job_status" in value:
        import capo_quicksight.types.asset_bundle_import_job_status

        out["JobStatus"] = (
            capo_quicksight.types.asset_bundle_import_job_status.serialize_json(
                value["job_status"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "asset_bundle_import_job_id" in value:
        out["AssetBundleImportJobId"] = value["asset_bundle_import_job_id"]
    if "failure_action" in value:
        import capo_quicksight.types.asset_bundle_import_failure_action

        out["FailureAction"] = (
            capo_quicksight.types.asset_bundle_import_failure_action.serialize_json(
                value["failure_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobSummary:
    out: AssetBundleImportJobSummary = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import capo_quicksight.types.asset_bundle_import_job_status

        out["job_status"] = (
            capo_quicksight.types.asset_bundle_import_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "AssetBundleImportJobId" in data:
        out["asset_bundle_import_job_id"] = data["AssetBundleImportJobId"]
    if "FailureAction" in data:
        import capo_quicksight.types.asset_bundle_import_failure_action

        out["failure_action"] = (
            capo_quicksight.types.asset_bundle_import_failure_action.deserialize_json(
                data["FailureAction"]
            )
        )
    return out
