"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_arn


class DescribeDatasetRequest(TypedDict):
    dataset_arn: "aws_sdk_rekognition.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset that you want to describe. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("DescribeDatasetRequest.dataset_arn required")
    return out
