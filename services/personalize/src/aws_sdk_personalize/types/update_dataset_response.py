"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class UpdateDatasetResponse(TypedDict):
    dataset_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset you updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDatasetResponse:
    out: UpdateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    return out
