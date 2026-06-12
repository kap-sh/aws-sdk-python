"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_arn
    import aws_sdk_sagemaker.types.job_category
    import aws_sdk_sagemaker.types.job_name
    import aws_sdk_sagemaker.types.job_secondary_status
    import aws_sdk_sagemaker.types.job_status
    import aws_sdk_sagemaker.types.timestamp


class JobSummary(TypedDict):
    job_arn: NotRequired["aws_sdk_sagemaker.types.job_arn.JobArn"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_name: NotRequired["aws_sdk_sagemaker.types.job_name.JobName"]
    """<p>The name of the job.</p>"""
    job_category: NotRequired["aws_sdk_sagemaker.types.job_category.JobCategory"]
    """<p>The category of the job.</p>"""
    job_status: NotRequired["aws_sdk_sagemaker.types.job_status.JobStatus"]
    """<p>The current status of the job.</p>"""
    job_secondary_status: NotRequired[
        "aws_sdk_sagemaker.types.job_secondary_status.JobSecondaryStatus"
    ]
    """<p>The secondary status of the job, providing more granular information about the job's progress. Secondary statuses may change between releases.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job was last modified.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the job ended.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_category" in value:
        import aws_sdk_sagemaker.types.job_category

        out["JobCategory"] = (
            aws_sdk_sagemaker.types.job_category.serialize_aws_json_1_1(
                value["job_category"]
            )
        )
    if "job_status" in value:
        import aws_sdk_sagemaker.types.job_status

        out["JobStatus"] = aws_sdk_sagemaker.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "job_secondary_status" in value:
        import aws_sdk_sagemaker.types.job_secondary_status

        out["JobSecondaryStatus"] = (
            aws_sdk_sagemaker.types.job_secondary_status.serialize_aws_json_1_1(
                value["job_secondary_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobCategory" in data:
        import aws_sdk_sagemaker.types.job_category

        out["job_category"] = (
            aws_sdk_sagemaker.types.job_category.deserialize_aws_json_1_1(
                data["JobCategory"]
            )
        )
    if "JobStatus" in data:
        import aws_sdk_sagemaker.types.job_status

        out["job_status"] = aws_sdk_sagemaker.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if "JobSecondaryStatus" in data:
        import aws_sdk_sagemaker.types.job_secondary_status

        out["job_secondary_status"] = (
            aws_sdk_sagemaker.types.job_secondary_status.deserialize_aws_json_1_1(
                data["JobSecondaryStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
