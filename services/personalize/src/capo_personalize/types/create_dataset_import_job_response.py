"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class CreateDatasetImportJobResponse(TypedDict, closed=True):
    dataset_import_job_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the dataset import job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetImportJobResponse) -> dict:
    out: dict = {}
    if "dataset_import_job_arn" in value:
        out["datasetImportJobArn"] = value["dataset_import_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetImportJobResponse:
    out: CreateDatasetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "datasetImportJobArn" in data:
        out["dataset_import_job_arn"] = data["datasetImportJobArn"]
    return out
