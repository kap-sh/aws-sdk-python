"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.job_attachment_settings
    import capo_deadline.types.job_id
    import capo_deadline.types.job_parameters
    import capo_deadline.types.job_run_as_user
    import capo_deadline.types.path_mapping_rules
    import capo_deadline.types.string


class JobDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    job_attachment_settings: NotRequired[
        "capo_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """<p>The job attachment settings.</p>"""
    job_run_as_user: NotRequired["capo_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>The user name and group that the job uses when run.</p>"""
    log_group_name: "capo_deadline.types.string.String"
    """<p>The log group name.</p>"""
    queue_role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The queue role ARN.</p>"""
    parameters: NotRequired["capo_deadline.types.job_parameters.JobParameters"]
    """<p>The parameters.</p>"""
    schema_version: "capo_deadline.types.string.String"
    """<p>The schema version.</p>"""
    path_mapping_rules: NotRequired[
        "capo_deadline.types.path_mapping_rules.PathMappingRules"
    ]
    """<p>The path mapping rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    if "job_attachment_settings" in value:
        import capo_deadline.types.job_attachment_settings

        out["jobAttachmentSettings"] = (
            capo_deadline.types.job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "job_run_as_user" in value:
        import capo_deadline.types.job_run_as_user

        out["jobRunAsUser"] = capo_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    out["logGroupName"] = value["log_group_name"]
    if "queue_role_arn" in value:
        out["queueRoleArn"] = value["queue_role_arn"]
    if "parameters" in value:
        import capo_deadline.types.job_parameters

        out["parameters"] = capo_deadline.types.job_parameters.serialize_json(
            value["parameters"]
        )
    out["schemaVersion"] = value["schema_version"]
    if "path_mapping_rules" in value:
        import capo_deadline.types.path_mapping_rules

        out["pathMappingRules"] = capo_deadline.types.path_mapping_rules.serialize_json(
            value["path_mapping_rules"]
        )
    return out


def deserialize_json(data: dict) -> JobDetailsEntity:
    out: JobDetailsEntity = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobDetailsEntity.job_id required")
    if "jobAttachmentSettings" in data:
        import capo_deadline.types.job_attachment_settings

        out["job_attachment_settings"] = (
            capo_deadline.types.job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if "jobRunAsUser" in data:
        import capo_deadline.types.job_run_as_user

        out["job_run_as_user"] = capo_deadline.types.job_run_as_user.deserialize_json(
            data["jobRunAsUser"]
        )
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("JobDetailsEntity.log_group_name required")
    if "queueRoleArn" in data:
        out["queue_role_arn"] = data["queueRoleArn"]
    if "parameters" in data:
        import capo_deadline.types.job_parameters

        out["parameters"] = capo_deadline.types.job_parameters.deserialize_json(
            data["parameters"]
        )
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("JobDetailsEntity.schema_version required")
    if "pathMappingRules" in data:
        import capo_deadline.types.path_mapping_rules

        out["path_mapping_rules"] = (
            capo_deadline.types.path_mapping_rules.deserialize_json(
                data["pathMappingRules"]
            )
        )
    return out
