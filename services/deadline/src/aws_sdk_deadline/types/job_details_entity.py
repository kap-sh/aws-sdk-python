"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.job_attachment_settings
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.job_parameters
    import aws_sdk_deadline.types.job_run_as_user
    import aws_sdk_deadline.types.path_mapping_rules
    import aws_sdk_deadline.types.string


class JobDetailsEntity(TypedDict, closed=True):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    job_attachment_settings: NotRequired[
        "aws_sdk_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """<p>The job attachment settings.</p>"""
    job_run_as_user: NotRequired["aws_sdk_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>The user name and group that the job uses when run.</p>"""
    log_group_name: "aws_sdk_deadline.types.string.String"
    """<p>The log group name.</p>"""
    queue_role_arn: NotRequired["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The queue role ARN.</p>"""
    parameters: NotRequired["aws_sdk_deadline.types.job_parameters.JobParameters"]
    """<p>The parameters.</p>"""
    schema_version: "aws_sdk_deadline.types.string.String"
    """<p>The schema version.</p>"""
    path_mapping_rules: NotRequired[
        "aws_sdk_deadline.types.path_mapping_rules.PathMappingRules"
    ]
    """<p>The path mapping rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    if "job_attachment_settings" in value:
        import aws_sdk_deadline.types.job_attachment_settings

        out["jobAttachmentSettings"] = (
            aws_sdk_deadline.types.job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "job_run_as_user" in value:
        import aws_sdk_deadline.types.job_run_as_user

        out["jobRunAsUser"] = aws_sdk_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    out["logGroupName"] = value["log_group_name"]
    if "queue_role_arn" in value:
        out["queueRoleArn"] = value["queue_role_arn"]
    if "parameters" in value:
        import aws_sdk_deadline.types.job_parameters

        out["parameters"] = aws_sdk_deadline.types.job_parameters.serialize_json(
            value["parameters"]
        )
    out["schemaVersion"] = value["schema_version"]
    if "path_mapping_rules" in value:
        import aws_sdk_deadline.types.path_mapping_rules

        out["pathMappingRules"] = (
            aws_sdk_deadline.types.path_mapping_rules.serialize_json(
                value["path_mapping_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobDetailsEntity:
    out: JobDetailsEntity = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobDetailsEntity.job_id required")
    if "jobAttachmentSettings" in data:
        import aws_sdk_deadline.types.job_attachment_settings

        out["job_attachment_settings"] = (
            aws_sdk_deadline.types.job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if "jobRunAsUser" in data:
        import aws_sdk_deadline.types.job_run_as_user

        out["job_run_as_user"] = (
            aws_sdk_deadline.types.job_run_as_user.deserialize_json(
                data["jobRunAsUser"]
            )
        )
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("JobDetailsEntity.log_group_name required")
    if "queueRoleArn" in data:
        out["queue_role_arn"] = data["queueRoleArn"]
    if "parameters" in data:
        import aws_sdk_deadline.types.job_parameters

        out["parameters"] = aws_sdk_deadline.types.job_parameters.deserialize_json(
            data["parameters"]
        )
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("JobDetailsEntity.schema_version required")
    if "pathMappingRules" in data:
        import aws_sdk_deadline.types.path_mapping_rules

        out["path_mapping_rules"] = (
            aws_sdk_deadline.types.path_mapping_rules.deserialize_json(
                data["pathMappingRules"]
            )
        )
    return out
