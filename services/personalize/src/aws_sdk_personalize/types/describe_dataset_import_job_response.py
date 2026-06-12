"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_import_job


class DescribeDatasetImportJobResponse(TypedDict):
    dataset_import_job: NotRequired[
        "aws_sdk_personalize.types.dataset_import_job.DatasetImportJob"
    ]
    """<p>Information about the dataset import job, including the status.</p> <p>The status is one of the following values:</p> <ul> <li> <p>CREATE PENDING</p> </li> <li> <p>CREATE IN_PROGRESS</p> </li> <li> <p>ACTIVE</p> </li> <li> <p>CREATE FAILED</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetImportJobResponse) -> dict:
    out: dict = {}
    if "dataset_import_job" in value:
        import aws_sdk_personalize.types.dataset_import_job

        out["datasetImportJob"] = (
            aws_sdk_personalize.types.dataset_import_job.serialize_aws_json_1_1(
                value["dataset_import_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetImportJobResponse:
    out: DescribeDatasetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "datasetImportJob" in data:
        import aws_sdk_personalize.types.dataset_import_job

        out["dataset_import_job"] = (
            aws_sdk_personalize.types.dataset_import_job.deserialize_aws_json_1_1(
                data["datasetImportJob"]
            )
        )
    return out
