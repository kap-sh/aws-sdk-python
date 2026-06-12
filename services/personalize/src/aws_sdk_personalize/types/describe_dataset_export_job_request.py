"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeDatasetExportJobRequest(TypedDict):
    dataset_export_job_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset export job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetExportJobRequest) -> dict:
    out: dict = {}
    out["datasetExportJobArn"] = value["dataset_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetExportJobRequest:
    out: DescribeDatasetExportJobRequest = {}  # type: ignore[typeddict-item]
    if "datasetExportJobArn" in data:
        out["dataset_export_job_arn"] = data["datasetExportJobArn"]
    else:
        raise DeserializationError(
            "DescribeDatasetExportJobRequest.dataset_export_job_arn required"
        )
    return out
