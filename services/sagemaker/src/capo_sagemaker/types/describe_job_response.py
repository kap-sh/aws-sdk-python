"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.job_arn
    import capo_sagemaker.types.job_category
    import capo_sagemaker.types.job_config_document
    import capo_sagemaker.types.job_name
    import capo_sagemaker.types.job_schema_version
    import capo_sagemaker.types.job_secondary_status
    import capo_sagemaker.types.job_secondary_status_transitions
    import capo_sagemaker.types.job_status
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp


class DescribeJobResponse(TypedDict, closed=True):
    job_name: NotRequired["capo_sagemaker.types.job_name.JobName"]
    """<p>The name of the job.</p>"""
    job_arn: NotRequired["capo_sagemaker.types.job_arn.JobArn"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role associated with the job.</p>"""
    job_category: NotRequired["capo_sagemaker.types.job_category.JobCategory"]
    """<p>The category of the job.</p>"""
    job_config_schema_version: NotRequired[
        "capo_sagemaker.types.job_schema_version.JobSchemaVersion"
    ]
    """<p>The schema version used for the job configuration document.</p>"""
    job_config_document: NotRequired[
        "capo_sagemaker.types.job_config_document.JobConfigDocument"
    ]
    """<p>The JSON configuration document for the job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job was last modified.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job ended.</p>"""
    job_status: NotRequired["capo_sagemaker.types.job_status.JobStatus"]
    """<p>The current status of the job.</p>"""
    secondary_status: NotRequired[
        "capo_sagemaker.types.job_secondary_status.JobSecondaryStatus"
    ]
    """<p>The detailed secondary status of the job, providing more granular information about the job's progress. Secondary statuses may change between releases.</p>"""
    secondary_status_transitions: NotRequired[
        "capo_sagemaker.types.job_secondary_status_transitions.JobSecondaryStatusTransitions"
    ]
    """<p>A list of secondary status transitions for the job, with timestamps and optional status messages.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the job failed, the reason it failed.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeJobResponse) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "job_category" in value:
        import capo_sagemaker.types.job_category

        out["JobCategory"] = capo_sagemaker.types.job_category.serialize_aws_json_1_1(
            value["job_category"]
        )
    if "job_config_schema_version" in value:
        out["JobConfigSchemaVersion"] = value["job_config_schema_version"]
    if "job_config_document" in value:
        out["JobConfigDocument"] = value["job_config_document"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "job_status" in value:
        import capo_sagemaker.types.job_status

        out["JobStatus"] = capo_sagemaker.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "secondary_status" in value:
        import capo_sagemaker.types.job_secondary_status

        out["SecondaryStatus"] = (
            capo_sagemaker.types.job_secondary_status.serialize_aws_json_1_1(
                value["secondary_status"]
            )
        )
    if "secondary_status_transitions" in value:
        import capo_sagemaker.types.job_secondary_status_transitions

        out["SecondaryStatusTransitions"] = (
            capo_sagemaker.types.job_secondary_status_transitions.serialize_aws_json_1_1(
                value["secondary_status_transitions"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeJobResponse:
    out: DescribeJobResponse = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "JobCategory" in data:
        import capo_sagemaker.types.job_category

        out["job_category"] = (
            capo_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    if "JobConfigSchemaVersion" in data:
        out["job_config_schema_version"] = data["JobConfigSchemaVersion"]
    if "JobConfigDocument" in data:
        out["job_config_document"] = data["JobConfigDocument"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "EndTime" in data:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "JobStatus" in data:
        import capo_sagemaker.types.job_status

        out["job_status"] = capo_sagemaker.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if "SecondaryStatus" in data:
        import capo_sagemaker.types.job_secondary_status

        out["secondary_status"] = (
            capo_sagemaker.types.job_secondary_status.deserialize_aws_json_1_1(
                data["SecondaryStatus"]
            )
        )
    if "SecondaryStatusTransitions" in data:
        import capo_sagemaker.types.job_secondary_status_transitions

        out["secondary_status_transitions"] = (
            capo_sagemaker.types.job_secondary_status_transitions.deserialize_aws_json_1_1(
                data["SecondaryStatusTransitions"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
