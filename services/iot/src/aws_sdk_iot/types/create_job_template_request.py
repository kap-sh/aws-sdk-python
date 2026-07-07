"""Generated from Smithy shape ``com.amazonaws.iot#CreateJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.abort_config
    import aws_sdk_iot.types.destination_package_versions
    import aws_sdk_iot.types.job_arn
    import aws_sdk_iot.types.job_description
    import aws_sdk_iot.types.job_document
    import aws_sdk_iot.types.job_document_source
    import aws_sdk_iot.types.job_executions_retry_config
    import aws_sdk_iot.types.job_executions_rollout_config
    import aws_sdk_iot.types.job_template_id
    import aws_sdk_iot.types.maintenance_windows
    import aws_sdk_iot.types.presigned_url_config
    import aws_sdk_iot.types.tag_list
    import aws_sdk_iot.types.timeout_config


class CreateJobTemplateRequest(TypedDict, closed=True):
    job_template_id: "aws_sdk_iot.types.job_template_id.JobTemplateId"
    r"""<p>A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, \"-\", and \"_\" are valid for use here.</p>"""
    job_arn: NotRequired["aws_sdk_iot.types.job_arn.JobArn"]
    """<p>The ARN of the job to use as the basis for the job template.</p>"""
    document_source: NotRequired[
        "aws_sdk_iot.types.job_document_source.JobDocumentSource"
    ]
    r"""<p>An S3 link, or S3 object URL, to the job document. The link is an Amazon S3 object URL and is required if you don't specify a value for <code>document</code>.</p> <p>For example, <code>--document-source https://s3.<i>region-code</i>.amazonaws.com/example-firmware/device-firmware.1.0</code> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html\">Methods for accessing a bucket</a>.</p>"""
    document: NotRequired["aws_sdk_iot.types.job_document.JobDocument"]
    """<p>The job document. Required if you don't specify a value for <code>documentSource</code>.</p>"""
    description: "aws_sdk_iot.types.job_description.JobDescription"
    """<p>A description of the job document.</p>"""
    presigned_url_config: NotRequired[
        "aws_sdk_iot.types.presigned_url_config.PresignedUrlConfig"
    ]
    job_executions_rollout_config: NotRequired[
        "aws_sdk_iot.types.job_executions_rollout_config.JobExecutionsRolloutConfig"
    ]
    abort_config: NotRequired["aws_sdk_iot.types.abort_config.AbortConfig"]
    timeout_config: NotRequired["aws_sdk_iot.types.timeout_config.TimeoutConfig"]
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the job template.</p>"""
    job_executions_retry_config: NotRequired[
        "aws_sdk_iot.types.job_executions_retry_config.JobExecutionsRetryConfig"
    ]
    """<p>Allows you to create the criteria to retry a job.</p>"""
    maintenance_windows: NotRequired[
        "aws_sdk_iot.types.maintenance_windows.MaintenanceWindows"
    ]
    """<p>Allows you to configure an optional maintenance window for the rollout of a job document to all devices in the target group for a job.</p>"""
    destination_package_versions: NotRequired[
        "aws_sdk_iot.types.destination_package_versions.DestinationPackageVersions"
    ]
    r"""<p>The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle\">Package version lifecycle</a>.</p> <p> <b>Note:</b>The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTemplateRequest) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "document_source" in value:
        out["documentSource"] = value["document_source"]
    if "document" in value:
        out["document"] = value["document"]
    out["description"] = value["description"]
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
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
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


def deserialize_json(data: dict) -> CreateJobTemplateRequest:
    out: CreateJobTemplateRequest = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "documentSource" in data:
        out["document_source"] = data["documentSource"]
    if "document" in data:
        out["document"] = data["document"]
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("CreateJobTemplateRequest.description required")
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
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
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
