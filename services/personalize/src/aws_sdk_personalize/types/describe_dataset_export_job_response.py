"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_export_job


class DescribeDatasetExportJobResponse(TypedDict):
    dataset_export_job: NotRequired[
        "aws_sdk_personalize.types.dataset_export_job.DatasetExportJob"
    ]
    """<p>Information about the dataset export job, including the status.</p> <p>The status is one of the following values:</p> <ul> <li> <p>CREATE PENDING</p> </li> <li> <p>CREATE IN_PROGRESS</p> </li> <li> <p>ACTIVE</p> </li> <li> <p>CREATE FAILED</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetExportJobResponse) -> dict:
    out: dict = {}
    if "dataset_export_job" in value:
        import aws_sdk_personalize.types.dataset_export_job

        out["datasetExportJob"] = (
            aws_sdk_personalize.types.dataset_export_job.serialize_aws_json_1_1(
                value["dataset_export_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetExportJobResponse:
    out: DescribeDatasetExportJobResponse = {}  # type: ignore[typeddict-item]
    if "datasetExportJob" in data:
        import aws_sdk_personalize.types.dataset_export_job

        out["dataset_export_job"] = (
            aws_sdk_personalize.types.dataset_export_job.deserialize_aws_json_1_1(
                data["datasetExportJob"]
            )
        )
    return out
