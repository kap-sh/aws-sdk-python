"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAssetBundleImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.asset_bundle_import_failure_action
    import aws_sdk_quicksight.types.asset_bundle_import_job_error_list
    import aws_sdk_quicksight.types.asset_bundle_import_job_override_parameters
    import aws_sdk_quicksight.types.asset_bundle_import_job_override_permissions
    import aws_sdk_quicksight.types.asset_bundle_import_job_override_tags
    import aws_sdk_quicksight.types.asset_bundle_import_job_override_validation_strategy
    import aws_sdk_quicksight.types.asset_bundle_import_job_status
    import aws_sdk_quicksight.types.asset_bundle_import_job_warning_list
    import aws_sdk_quicksight.types.asset_bundle_import_source_description
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.timestamp


class DescribeAssetBundleImportJobResponse(TypedDict):
    job_status: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_status.AssetBundleImportJobStatus"
    ]
    """<p>Indicates the status of a job through its queuing and execution.</p> <p>Poll the <code>DescribeAssetBundleImport</code> API until <code>JobStatus</code> returns one of the following values:</p> <ul> <li> <p> <code>SUCCESSFUL</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>FAILED_ROLLBACK_COMPLETED</code> </p> </li> <li> <p> <code>FAILED_ROLLBACK_ERROR</code> </p> </li> </ul>"""
    errors: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_error_list.AssetBundleImportJobErrorList"
    ]
    """<p>An array of error records that describes any failures that occurred during the export job processing.</p> <p>Error records accumulate while the job is still running. The complete set of error records is available after the job has completed and failed.</p>"""
    rollback_errors: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_error_list.AssetBundleImportJobErrorList"
    ]
    """<p>An array of error records that describes any failures that occurred while an import job was attempting a rollback.</p> <p>Error records accumulate while the job is still running. The complete set of error records is available after the job has completed and failed.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the import job.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the import job was created.</p>"""
    asset_bundle_import_job_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. The job ID is set when you start a new job with a <code>StartAssetBundleImportJob</code> API call.</p>"""
    aws_account_id: NotRequired["aws_sdk_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account the import job was executed in. </p>"""
    asset_bundle_import_source: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_source_description.AssetBundleImportSourceDescription"
    ]
    """<p>The source of the asset bundle zip file that contains the data that is imported by the job.</p>"""
    override_parameters: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_override_parameters.AssetBundleImportJobOverrideParameters"
    ]
    """<p>Optional overrides that are applied to the resource configuration before import.</p>"""
    failure_action: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_failure_action.AssetBundleImportFailureAction"
    ]
    """<p>The failure action for the import job.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the response.</p>"""
    override_permissions: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_override_permissions.AssetBundleImportJobOverridePermissions"
    ]
    """<p>Optional permission overrides that are applied to the resource configuration before import.</p>"""
    override_tags: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_override_tags.AssetBundleImportJobOverrideTags"
    ]
    """<p>Optional tag overrides that are applied to the resource configuration before import.</p>"""
    override_validation_strategy: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_override_validation_strategy.AssetBundleImportJobOverrideValidationStrategy"
    ]
    """<p>An optional validation strategy override for all analyses and dashboards to be applied to the resource configuration before import.</p>"""
    warnings: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_import_job_warning_list.AssetBundleImportJobWarningList"
    ]
    """<p>An array of warning records that describe all permitted errors that are encountered during the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetBundleImportJobResponse) -> dict:
    out: dict = {}
    if "job_status" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_status

        out["JobStatus"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_status.serialize_json(
                value["job_status"]
            )
        )
    if "errors" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_error_list

        out["Errors"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_error_list.serialize_json(
                value["errors"]
            )
        )
    if "rollback_errors" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_error_list

        out["RollbackErrors"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_error_list.serialize_json(
                value["rollback_errors"]
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
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "asset_bundle_import_source" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_source_description

        out["AssetBundleImportSource"] = (
            aws_sdk_quicksight.types.asset_bundle_import_source_description.serialize_json(
                value["asset_bundle_import_source"]
            )
        )
    if "override_parameters" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_parameters

        out["OverrideParameters"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_parameters.serialize_json(
                value["override_parameters"]
            )
        )
    if "failure_action" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_failure_action

        out["FailureAction"] = (
            aws_sdk_quicksight.types.asset_bundle_import_failure_action.serialize_json(
                value["failure_action"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "override_permissions" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_permissions

        out["OverridePermissions"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_permissions.serialize_json(
                value["override_permissions"]
            )
        )
    if "override_tags" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_tags

        out["OverrideTags"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_tags.serialize_json(
                value["override_tags"]
            )
        )
    if "override_validation_strategy" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_validation_strategy

        out["OverrideValidationStrategy"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_validation_strategy.serialize_json(
                value["override_validation_strategy"]
            )
        )
    if "warnings" in value:
        import aws_sdk_quicksight.types.asset_bundle_import_job_warning_list

        out["Warnings"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_warning_list.serialize_json(
                value["warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAssetBundleImportJobResponse:
    out: DescribeAssetBundleImportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_status

        out["job_status"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_status.deserialize_json(
                data["JobStatus"]
            )
        )
    if "Errors" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_error_list

        out["errors"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if "RollbackErrors" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_error_list

        out["rollback_errors"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_error_list.deserialize_json(
                data["RollbackErrors"]
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
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "AssetBundleImportSource" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_source_description

        out["asset_bundle_import_source"] = (
            aws_sdk_quicksight.types.asset_bundle_import_source_description.deserialize_json(
                data["AssetBundleImportSource"]
            )
        )
    if "OverrideParameters" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_parameters

        out["override_parameters"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_parameters.deserialize_json(
                data["OverrideParameters"]
            )
        )
    if "FailureAction" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_failure_action

        out["failure_action"] = (
            aws_sdk_quicksight.types.asset_bundle_import_failure_action.deserialize_json(
                data["FailureAction"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "OverridePermissions" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_permissions

        out["override_permissions"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_permissions.deserialize_json(
                data["OverridePermissions"]
            )
        )
    if "OverrideTags" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_tags

        out["override_tags"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_tags.deserialize_json(
                data["OverrideTags"]
            )
        )
    if "OverrideValidationStrategy" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_override_validation_strategy

        out["override_validation_strategy"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_override_validation_strategy.deserialize_json(
                data["OverrideValidationStrategy"]
            )
        )
    if "Warnings" in data:
        import aws_sdk_quicksight.types.asset_bundle_import_job_warning_list

        out["warnings"] = (
            aws_sdk_quicksight.types.asset_bundle_import_job_warning_list.deserialize_json(
                data["Warnings"]
            )
        )
    return out
