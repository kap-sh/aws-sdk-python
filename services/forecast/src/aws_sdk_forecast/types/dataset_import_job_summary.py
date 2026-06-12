"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetImportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.data_source
    import aws_sdk_forecast.types.error_message
    import aws_sdk_forecast.types.import_mode
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class DatasetImportJobSummary(TypedDict):
    dataset_import_job_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset import job.</p>"""
    dataset_import_job_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the dataset import job.</p>"""
    data_source: NotRequired["aws_sdk_forecast.types.data_source.DataSource"]
    """<p>The location of the training data to import and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data. The training data must be stored in an Amazon S3 bucket.</p> <p>If encryption is used, <code>DataSource</code> includes an Key Management Service (KMS) key.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the dataset import job. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> </ul>"""
    message: NotRequired["aws_sdk_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset import job was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    import_mode: NotRequired["aws_sdk_forecast.types.import_mode.ImportMode"]
    """<p>The import mode of the dataset import job, FULL or INCREMENTAL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetImportJobSummary) -> dict:
    out: dict = {}
    if "dataset_import_job_arn" in value:
        out["DatasetImportJobArn"] = value["dataset_import_job_arn"]
    if "dataset_import_job_name" in value:
        out["DatasetImportJobName"] = value["dataset_import_job_name"]
    if "data_source" in value:
        import aws_sdk_forecast.types.data_source

        out["DataSource"] = aws_sdk_forecast.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["CreationTime"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["LastModificationTime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    if "import_mode" in value:
        import aws_sdk_forecast.types.import_mode

        out["ImportMode"] = aws_sdk_forecast.types.import_mode.serialize_aws_json_1_1(
            value["import_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetImportJobSummary:
    out: DatasetImportJobSummary = {}  # type: ignore[typeddict-item]
    if "DatasetImportJobArn" in data:
        out["dataset_import_job_arn"] = data["DatasetImportJobArn"]
    if "DatasetImportJobName" in data:
        out["dataset_import_job_name"] = data["DatasetImportJobName"]
    if "DataSource" in data:
        import aws_sdk_forecast.types.data_source

        out["data_source"] = (
            aws_sdk_forecast.types.data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["creation_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModificationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    if "ImportMode" in data:
        import aws_sdk_forecast.types.import_mode

        out["import_mode"] = (
            aws_sdk_forecast.types.import_mode.deserialize_aws_json_1_1(
                data["ImportMode"]
            )
        )
    return out
