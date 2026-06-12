"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetImportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.import_mode
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status


class DatasetImportJobSummary(TypedDict):
    dataset_import_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset import job.</p>"""
    job_name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the dataset import job.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the dataset import job.</p> <p>A dataset import job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the dataset import job was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the dataset import job status was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a dataset import job fails, the reason behind the failure.</p>"""
    import_mode: NotRequired["aws_sdk_personalize.types.import_mode.ImportMode"]
    """<p>The import mode the dataset import job used to update the data in the dataset. For more information see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/updating-existing-bulk-data.html\">Updating existing bulk data</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetImportJobSummary) -> dict:
    out: dict = {}
    if "dataset_import_job_arn" in value:
        out["datasetImportJobArn"] = value["dataset_import_job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "status" in value:
        out["status"] = value["status"]
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
    if "import_mode" in value:
        import aws_sdk_personalize.types.import_mode

        out["importMode"] = (
            aws_sdk_personalize.types.import_mode.serialize_aws_json_1_1(
                value["import_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetImportJobSummary:
    out: DatasetImportJobSummary = {}  # type: ignore[typeddict-item]
    if "datasetImportJobArn" in data:
        out["dataset_import_job_arn"] = data["datasetImportJobArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "status" in data:
        out["status"] = data["status"]
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
    if "importMode" in data:
        import aws_sdk_personalize.types.import_mode

        out["import_mode"] = (
            aws_sdk_personalize.types.import_mode.deserialize_aws_json_1_1(
                data["importMode"]
            )
        )
    return out
