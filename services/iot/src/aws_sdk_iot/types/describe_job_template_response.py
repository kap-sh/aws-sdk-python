"""Generated from Smithy shape ``com.amazonaws.iot#DescribeJobTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.abort_config
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.destination_package_versions
    import aws_sdk_iot.types.job_description
    import aws_sdk_iot.types.job_document
    import aws_sdk_iot.types.job_document_source
    import aws_sdk_iot.types.job_executions_retry_config
    import aws_sdk_iot.types.job_executions_rollout_config
    import aws_sdk_iot.types.job_template_arn
    import aws_sdk_iot.types.job_template_id
    import aws_sdk_iot.types.maintenance_windows
    import aws_sdk_iot.types.presigned_url_config
    import aws_sdk_iot.types.timeout_config


class DescribeJobTemplateResponse(TypedDict):
    job_template_arn: NotRequired["aws_sdk_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template.</p>"""
    job_template_id: NotRequired["aws_sdk_iot.types.job_template_id.JobTemplateId"]
    """<p>The unique identifier of the job template.</p>"""
    description: NotRequired["aws_sdk_iot.types.job_description.JobDescription"]
    """<p>A description of the job template.</p>"""
    document_source: NotRequired[
        "aws_sdk_iot.types.job_document_source.JobDocumentSource"
    ]
    """<p>An S3 link to the job document.</p>"""
    document: NotRequired["aws_sdk_iot.types.job_document.JobDocument"]
    """<p>The job document.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job template was created.</p>"""
    presigned_url_config: NotRequired[
        "aws_sdk_iot.types.presigned_url_config.PresignedUrlConfig"
    ]
    job_executions_rollout_config: NotRequired[
        "aws_sdk_iot.types.job_executions_rollout_config.JobExecutionsRolloutConfig"
    ]
    abort_config: NotRequired["aws_sdk_iot.types.abort_config.AbortConfig"]
    timeout_config: NotRequired["aws_sdk_iot.types.timeout_config.TimeoutConfig"]
    job_executions_retry_config: NotRequired[
        "aws_sdk_iot.types.job_executions_retry_config.JobExecutionsRetryConfig"
    ]
    """<p>The configuration that determines how many retries are allowed for each failure type for a job.</p>"""
    maintenance_windows: NotRequired[
        "aws_sdk_iot.types.maintenance_windows.MaintenanceWindows"
    ]
    """<p>Allows you to configure an optional maintenance window for the rollout of a job document to all devices in the target group for a job.</p>"""
    destination_package_versions: NotRequired[
        "aws_sdk_iot.types.destination_package_versions.DestinationPackageVersions"
    ]
    r"""<p>The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle\">Package version lifecycle</a>.</p> <p> <b>Note:</b>The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobTemplateResponse) -> dict:
    out: dict = {}
    if "job_template_arn" in value:
        out["jobTemplateArn"] = value["job_template_arn"]
    if "job_template_id" in value:
        out["jobTemplateId"] = value["job_template_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "document_source" in value:
        out["documentSource"] = value["document_source"]
    if "document" in value:
        out["document"] = value["document"]
    if "created_at" in value:
        import aws_sdk_iot.types.date_type

        out["createdAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["created_at"]
        )
    if "presigned_url_config" in value:
        import aws_sdk_iot.types.presigned_url_config

        out["presignedUrlConfig"] = (
            aws_sdk_iot.types.presigned_url_config.serialize_json(
                value["presigned_url_config"]
            )
        )
    if "job_executions_rollout_config" in value:
        import aws_sdk_iot.types.job_executions_rollout_config

        out["jobExecutionsRolloutConfig"] = (
            aws_sdk_iot.types.job_executions_rollout_config.serialize_json(
                value["job_executions_rollout_config"]
            )
        )
    if "abort_config" in value:
        import aws_sdk_iot.types.abort_config

        out["abortConfig"] = aws_sdk_iot.types.abort_config.serialize_json(
            value["abort_config"]
        )
    if "timeout_config" in value:
        import aws_sdk_iot.types.timeout_config

        out["timeoutConfig"] = aws_sdk_iot.types.timeout_config.serialize_json(
            value["timeout_config"]
        )
    if "job_executions_retry_config" in value:
        import aws_sdk_iot.types.job_executions_retry_config

        out["jobExecutionsRetryConfig"] = (
            aws_sdk_iot.types.job_executions_retry_config.serialize_json(
                value["job_executions_retry_config"]
            )
        )
    if "maintenance_windows" in value:
        import aws_sdk_iot.types.maintenance_windows

        out["maintenanceWindows"] = (
            aws_sdk_iot.types.maintenance_windows.serialize_json(
                value["maintenance_windows"]
            )
        )
    if "destination_package_versions" in value:
        import aws_sdk_iot.types.destination_package_versions

        out["destinationPackageVersions"] = (
            aws_sdk_iot.types.destination_package_versions.serialize_json(
                value["destination_package_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeJobTemplateResponse:
    out: DescribeJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplateArn" in data:
        out["job_template_arn"] = data["jobTemplateArn"]
    if "jobTemplateId" in data:
        out["job_template_id"] = data["jobTemplateId"]
    if "description" in data:
        out["description"] = data["description"]
    if "documentSource" in data:
        out["document_source"] = data["documentSource"]
    if "document" in data:
        out["document"] = data["document"]
    if "createdAt" in data:
        import aws_sdk_iot.types.date_type

        out["created_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createdAt"]
        )
    if "presignedUrlConfig" in data:
        import aws_sdk_iot.types.presigned_url_config

        out["presigned_url_config"] = (
            aws_sdk_iot.types.presigned_url_config.deserialize_json(
                data["presignedUrlConfig"]
            )
        )
    if "jobExecutionsRolloutConfig" in data:
        import aws_sdk_iot.types.job_executions_rollout_config

        out["job_executions_rollout_config"] = (
            aws_sdk_iot.types.job_executions_rollout_config.deserialize_json(
                data["jobExecutionsRolloutConfig"]
            )
        )
    if "abortConfig" in data:
        import aws_sdk_iot.types.abort_config

        out["abort_config"] = aws_sdk_iot.types.abort_config.deserialize_json(
            data["abortConfig"]
        )
    if "timeoutConfig" in data:
        import aws_sdk_iot.types.timeout_config

        out["timeout_config"] = aws_sdk_iot.types.timeout_config.deserialize_json(
            data["timeoutConfig"]
        )
    if "jobExecutionsRetryConfig" in data:
        import aws_sdk_iot.types.job_executions_retry_config

        out["job_executions_retry_config"] = (
            aws_sdk_iot.types.job_executions_retry_config.deserialize_json(
                data["jobExecutionsRetryConfig"]
            )
        )
    if "maintenanceWindows" in data:
        import aws_sdk_iot.types.maintenance_windows

        out["maintenance_windows"] = (
            aws_sdk_iot.types.maintenance_windows.deserialize_json(
                data["maintenanceWindows"]
            )
        )
    if "destinationPackageVersions" in data:
        import aws_sdk_iot.types.destination_package_versions

        out["destination_package_versions"] = (
            aws_sdk_iot.types.destination_package_versions.deserialize_json(
                data["destinationPackageVersions"]
            )
        )
    return out
