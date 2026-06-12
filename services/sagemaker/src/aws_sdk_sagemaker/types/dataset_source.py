"""Generated from Smithy shape ``com.amazonaws.sagemaker#DatasetSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_data_set_arn


class DatasetSource(TypedDict):
    dataset_arn: "aws_sdk_sagemaker.types.hub_data_set_arn.HubDataSetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetSource) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetSource:
    out: DatasetSource = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("DatasetSource.dataset_arn required")
    return out
