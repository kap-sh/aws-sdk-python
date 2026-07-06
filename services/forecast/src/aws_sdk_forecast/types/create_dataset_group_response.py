"""Generated from Smithy shape ``com.amazonaws.forecast#CreateDatasetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreateDatasetGroupResponse(TypedDict, closed=True):
    dataset_group_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetGroupResponse) -> dict:
    out: dict = {}
    if "dataset_group_arn" in value:
        out["DatasetGroupArn"] = value["dataset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetGroupResponse:
    out: CreateDatasetGroupResponse = {}  # type: ignore[typeddict-item]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    return out
