"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeDatasetImportJobRequest(TypedDict):
    dataset_import_job_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset import job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetImportJobRequest) -> dict:
    out: dict = {}
    out["datasetImportJobArn"] = value["dataset_import_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetImportJobRequest:
    out: DescribeDatasetImportJobRequest = {}  # type: ignore[typeddict-item]
    if "datasetImportJobArn" in data:
        out["dataset_import_job_arn"] = data["datasetImportJobArn"]
    else:
        raise DeserializationError(
            "DescribeDatasetImportJobRequest.dataset_import_job_arn required"
        )
    return out
