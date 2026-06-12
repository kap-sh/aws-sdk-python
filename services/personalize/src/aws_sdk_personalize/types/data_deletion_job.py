"""Generated from Smithy shape ``com.amazonaws.personalize#DataDeletionJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.data_source
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.integer
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.role_arn
    import aws_sdk_personalize.types.status


class DataDeletionJob(TypedDict):
    job_name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the data deletion job.</p>"""
    data_deletion_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data deletion job.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group the job deletes records from.</p>"""
    data_source: NotRequired["aws_sdk_personalize.types.data_source.DataSource"]
    role_arn: NotRequired["aws_sdk_personalize.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the data deletion job.</p> <p>A data deletion job can have one of the following statuses:</p> <ul> <li> <p>PENDING > IN_PROGRESS > COMPLETED -or- FAILED</p> </li> </ul>"""
    num_deleted: NotRequired["aws_sdk_personalize.types.integer.Integer"]
    """<p>The number of records deleted by a COMPLETED job.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the data deletion job.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) the data deletion job was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a data deletion job fails, provides the reason why.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataDeletionJob) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "data_deletion_job_arn" in value:
        out["dataDeletionJobArn"] = value["data_deletion_job_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "data_source" in value:
        import aws_sdk_personalize.types.data_source

        out["dataSource"] = (
            aws_sdk_personalize.types.data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "num_deleted" in value:
        out["numDeleted"] = value["num_deleted"]
    if "creation_date_time" in value:
        import aws_sdk_personalize.types.date

        out["creationDateTime"] = aws_sdk_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_personalize.types.date

        out["lastUpdatedDateTime"] = (
            aws_sdk_personalize.types.date.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataDeletionJob:
    out: DataDeletionJob = {}  # type: ignore[typeddict-item]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "dataDeletionJobArn" in data:
        out["data_deletion_job_arn"] = data["dataDeletionJobArn"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "dataSource" in data:
        import aws_sdk_personalize.types.data_source

        out["data_source"] = (
            aws_sdk_personalize.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "numDeleted" in data:
        out["num_deleted"] = data["numDeleted"]
    if "creationDateTime" in data:
        import aws_sdk_personalize.types.date

        out["creation_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_personalize.types.date

        out["last_updated_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
