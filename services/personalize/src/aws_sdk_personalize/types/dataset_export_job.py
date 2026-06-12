"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetExportJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.dataset_export_job_output
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.ingestion_mode
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status


class DatasetExportJob(TypedDict):
    job_name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the export job.</p>"""
    dataset_export_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset export job.</p>"""
    dataset_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset to export.</p>"""
    ingestion_mode: NotRequired[
        "aws_sdk_personalize.types.ingestion_mode.IngestionMode"
    ]
    """<p>The data to export, based on how you imported the data. You can choose to export <code>BULK</code> data that you imported using a dataset import job, <code>PUT</code> data that you imported incrementally (using the console, PutEvents, PutUsers and PutItems operations), or <code>ALL</code> for both types. The default value is <code>PUT</code>. </p>"""
    role_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM service role that has permissions to add data to your output Amazon S3 bucket.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the dataset export job.</p> <p>A dataset export job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul>"""
    job_output: NotRequired[
        "aws_sdk_personalize.types.dataset_export_job_output.DatasetExportJobOutput"
    ]
    """<p>The path to the Amazon S3 bucket where the job's output is stored. For example:</p> <p> <code>s3://bucket-name/folder-name/</code> </p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the dataset export job.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) the status of the dataset export job was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a dataset export job fails, provides the reason why.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetExportJob) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "dataset_export_job_arn" in value:
        out["datasetExportJobArn"] = value["dataset_export_job_arn"]
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "ingestion_mode" in value:
        import aws_sdk_personalize.types.ingestion_mode

        out["ingestionMode"] = (
            aws_sdk_personalize.types.ingestion_mode.serialize_aws_json_1_1(
                value["ingestion_mode"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "job_output" in value:
        import aws_sdk_personalize.types.dataset_export_job_output

        out["jobOutput"] = (
            aws_sdk_personalize.types.dataset_export_job_output.serialize_aws_json_1_1(
                value["job_output"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> DatasetExportJob:
    out: DatasetExportJob = {}  # type: ignore[typeddict-item]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "datasetExportJobArn" in data:
        out["dataset_export_job_arn"] = data["datasetExportJobArn"]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    if "ingestionMode" in data:
        import aws_sdk_personalize.types.ingestion_mode

        out["ingestion_mode"] = (
            aws_sdk_personalize.types.ingestion_mode.deserialize_aws_json_1_1(
                data["ingestionMode"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "jobOutput" in data:
        import aws_sdk_personalize.types.dataset_export_job_output

        out["job_output"] = (
            aws_sdk_personalize.types.dataset_export_job_output.deserialize_aws_json_1_1(
                data["jobOutput"]
            )
        )
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
