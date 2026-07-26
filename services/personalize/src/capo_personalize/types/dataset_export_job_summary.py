"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.name
    import capo_personalize.types.status


class DatasetExportJobSummary(TypedDict, closed=True):
    dataset_export_job_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset export job.</p>"""
    job_name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the dataset export job.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the dataset export job.</p> <p>A dataset export job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the dataset export job was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the dataset export job status was last updated.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a dataset export job fails, the reason behind the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetExportJobSummary) -> dict:
    out: dict = {}
    if "dataset_export_job_arn" in value:
        out["datasetExportJobArn"] = value["dataset_export_job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetExportJobSummary:
    out: DatasetExportJobSummary = {}  # type: ignore[typeddict-item]
    if "datasetExportJobArn" in data:
        out["dataset_export_job_arn"] = data["datasetExportJobArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
