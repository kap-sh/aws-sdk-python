"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ImportDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.dataset_arn
    import aws_sdk_lookoutequipment.types.dataset_name
    import aws_sdk_lookoutequipment.types.dataset_status
    import aws_sdk_lookoutequipment.types.ingestion_job_id


class ImportDatasetResponse(TypedDict, closed=True):
    dataset_name: NotRequired["aws_sdk_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the created machine learning dataset.</p>"""
    dataset_arn: NotRequired["aws_sdk_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resource Name (ARN) of the dataset that was imported.</p>"""
    status: NotRequired["aws_sdk_lookoutequipment.types.dataset_status.DatasetStatus"]
    """<p>The status of the <code>ImportDataset</code> operation.</p>"""
    job_id: NotRequired[
        "aws_sdk_lookoutequipment.types.ingestion_job_id.IngestionJobId"
    ]
    """<p>A unique identifier for the job of importing the dataset.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.dataset_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.dataset_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDatasetResponse:
    out: ImportDatasetResponse = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.dataset_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.dataset_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
