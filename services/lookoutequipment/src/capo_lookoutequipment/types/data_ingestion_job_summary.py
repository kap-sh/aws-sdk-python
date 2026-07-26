"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DataIngestionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.ingestion_input_configuration
    import capo_lookoutequipment.types.ingestion_job_id
    import capo_lookoutequipment.types.ingestion_job_status


class DataIngestionJobSummary(TypedDict, closed=True):
    job_id: NotRequired["capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"]
    """<p>Indicates the job ID of the data ingestion job. </p>"""
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset used for the data ingestion job. </p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resource Name (ARN) of the dataset used in the data ingestion job. </p>"""
    ingestion_input_configuration: NotRequired[
        "capo_lookoutequipment.types.ingestion_input_configuration.IngestionInputConfiguration"
    ]
    """<p> Specifies information for the input data for the data inference job, including data Amazon S3 location parameters. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>Indicates the status of the data ingestion job. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataIngestionJobSummary) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "ingestion_input_configuration" in value:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["IngestionInputConfiguration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.serialize_aws_json_1_0(
                value["ingestion_input_configuration"]
            )
        )
    if "status" in value:
        import capo_lookoutequipment.types.ingestion_job_status

        out["Status"] = (
            capo_lookoutequipment.types.ingestion_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataIngestionJobSummary:
    out: DataIngestionJobSummary = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "IngestionInputConfiguration" in data:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["ingestion_input_configuration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.deserialize_aws_json_1_0(
                data["IngestionInputConfiguration"]
            )
        )
    if "Status" in data:
        import capo_lookoutequipment.types.ingestion_job_status

        out["status"] = (
            capo_lookoutequipment.types.ingestion_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
