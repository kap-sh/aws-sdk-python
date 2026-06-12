"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteDatasetImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeleteDatasetImportJobRequest(TypedDict):
    dataset_import_job_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset import job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatasetImportJobRequest) -> dict:
    out: dict = {}
    out["DatasetImportJobArn"] = value["dataset_import_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatasetImportJobRequest:
    out: DeleteDatasetImportJobRequest = {}  # type: ignore[typeddict-item]
    if "DatasetImportJobArn" in data:
        out["dataset_import_job_arn"] = data["DatasetImportJobArn"]
    else:
        raise DeserializationError(
            "DeleteDatasetImportJobRequest.dataset_import_job_arn required"
        )
    return out
