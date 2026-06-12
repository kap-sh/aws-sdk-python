"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateDatasetExportJobResponse(TypedDict):
    dataset_export_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset export job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetExportJobResponse) -> dict:
    out: dict = {}
    if "dataset_export_job_arn" in value:
        out["datasetExportJobArn"] = value["dataset_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetExportJobResponse:
    out: CreateDatasetExportJobResponse = {}  # type: ignore[typeddict-item]
    if "datasetExportJobArn" in data:
        out["dataset_export_job_arn"] = data["datasetExportJobArn"]
    return out
