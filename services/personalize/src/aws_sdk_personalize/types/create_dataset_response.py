"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateDatasetResponse(TypedDict, closed=True):
    dataset_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    return out
